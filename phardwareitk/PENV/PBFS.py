import os
import sys
import time
import struct
import uuid

"""Minimum Disk size = 364 bytes, Maximum 6000+ Petabytes"""

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

PBFS_MAGIC: bytes = b"PBFS\x00\x00"
Block_SIZE: int = 512
Total_BLOCKS: int = 2048  # 1 MB
DISK_NAME: bytes = b"PBFS_PENV-PHardwareITK\x00\x00"
DISK_PATH: str = os.path.join(base_path, ".hard_disk", "vdrive.pbfs")
PBFS_VERSION: int = 1
First_boot_timestamp: int = 0  # 0 means no boot yet
OS_boot_mode: int = (
	0  # 0: Potato mode: Low resource mode, 1: Full Mode, 2: Recovery Mode
)
OS_boot_mode_str: str = (
	"Potato Mode"  # Default mode is Potato Mode, can be changed later
)

# 68-bytes
PBFS_HEADER_FORMAT: str = (
	"<6sII24sQIQHII"  # PBFS_MAGIC, block_size, total_blocks, disk_name, timestamp, version, first_boot_timestamp, os_boot_mode, File Table Offset, entries
)
FILE_TABLE_ENTRY_FORMAT: str = (
	"<128sqQQI"  # File name/path (128 bytes), file offset part 1 (8 bytes), file offset part 2 (8 bytes) (total 16 bytes), file data block span (8 bytes), Permission_Table_Offset: 4 bytes, Total = 156 bytes
)

PERMISSION_TABLE_ENTRY_FORMAT: str = (
	"<QI" # Permissions in int (8 bytes), File Names tree entry offset (4 bytes), Total = 12 bytes
)

FILE_TREE_ENTRY_OFFSET: str = (
	"<128s" # File Name (128 bytes), Total = 128 bytes
)

class PBFS_SuperBlock:
	def __init__(self) -> None:
		self.magic: bytes = PBFS_MAGIC
		self.version: int = 1
		self.block_size: int = Block_SIZE
		self.total_blocks: int = Total_BLOCKS
		self.disk_name: bytes = DISK_NAME
		self.disk_path: str = DISK_PATH
		self.timestamp: int = int(time.time())
		self.First_boot_timestamp: int = First_boot_timestamp  # 0 means no boot yet
		self.OS_boot_mode: int = (
			OS_boot_mode  # 0: Potato mode, 1: Full Mode, 2: Recovery Mode
		)
		self.file_table_offset: int = 68  # Offset for the file table
		self.entries: int = 0  # Number of entries in the file table

	def to_bytes(self) -> bytes:
		header = struct.pack(
			PBFS_HEADER_FORMAT,
			self.magic,
			self.block_size,
			self.total_blocks,
			self.disk_name,
			self.timestamp,
			self.version,
			self.First_boot_timestamp,
			self.OS_boot_mode,
			self.file_table_offset,
			self.entries,
		)
		return header

	def from_bytes(self, data: bytes) -> None:
		"""Reads the PBFS superblock from bytes."""
		unpacked_data = struct.unpack(PBFS_HEADER_FORMAT, data)
		self.magic = unpacked_data[0]
		self.block_size = unpacked_data[1]
		self.total_blocks = unpacked_data[2]
		self.disk_name = unpacked_data[3]
		self.timestamp = unpacked_data[4]
		self.version = unpacked_data[5]
		self.First_boot_timestamp = unpacked_data[6]
		self.OS_boot_mode = unpacked_data[7]
		self.file_table_offset = unpacked_data[8]
		self.entries = unpacked_data[9]

class PBFS_DriveData:
	def __init__(self):
		self.super_block = PBFS_SuperBlock()
		self.drive_data_path = os.path.join(base_path, ".hard_disk", "drive_data.pbfs")
		self.free_blocks = []  # Track available blocks for expansion of drive itself
		self.files:list = []
		self.dirs:list = []
		self.ftentrysize = 156
		self.headersize = 68
		self.permissiontsize = 12
		self.ftreeentrysize = 128
		# Total per entry = 364 bytes
		# 18,446,744,073,709,551,615 = max value, 6000+ Peta bytes
		self.dummy_offset:int = -1  # Dummy offset for files with no data, used to mark empty files

	def write_base_data(self) -> None:
		"""Writes the base data to the drive data file."""
		hdr: bytes = self.super_block.to_bytes()
		with open(self.drive_data_path, "wb") as f:
			f.seek(0)  # Ensure we write from the start
			f.write(hdr)

	def align_offset(self, offset: int) -> int:
		"""Aligns the offset to the nearest block size."""
		return (offset + self.super_block.block_size - 1) // self.super_block.block_size * self.super_block.block_size

	def pad_data(self, data:bytes) -> bytes:
		"""Pads the data to the nearest block size."""
		return data.ljust((len(data) + self.super_block.block_size - 1) // self.super_block.block_size * self.super_block.block_size, b'\x00')

	def check_free_block(self, offset: int, data: bytes) -> int:
		"""Checks for a free block in the drive data file."""
		# Go to the offset, skip the block and check if the next block is free
		data = data[offset:] # Read data from the offset
		block_size = self.super_block.block_size
		for i in range(0, len(data), block_size):
			if data[i:i + block_size] == b'\x00' * block_size:
				# Found a free block
				return offset + i

		return None  # No free block found

	def write_file(self, file_name: bytes, file_data: bytes, permissions:list=[0x0, 0x1, [None]]) -> int:
		"""Writes a file to the drive data file."""
		# Structure ->
		# [PBFS Header] -> Contains all the metadata about the drive
		# [File Table] -> Contains all file names and their offsets
		# [File Data] -> Contains the actual file data
		# Check if file headers are present
		dummy:bool = False

		if file_data == b"":
			dummy = True

		data: bytes = None
		try:
			with open(self.drive_data_path, "rb") as f:
				f.seek(0)  # Ensure we read from the start
				data = f.read()

		except FileNotFoundError:
			init_vdrive(False, True)
			if not os.path.exists(self.drive_data_path):
				return -220
			return self.write_file(file_name, file_data)  # Re-call this func after initializing the drive data file

		if not dummy:
			file_data = self.pad_data(file_data)  # Pad the file data to the nearest block size
		file_name = file_name.ljust(128, b'\x00') # Pad the file name to 128 bytes

		# Go to file table offset via the header
		self.super_block.from_bytes(data[:self.header_size])  # Read the superblock from the first 68 bytes
		file_table_offset = self.super_block.file_table_offset
		entries = self.super_block.entries

		file_table_data = data[file_table_offset:]  # Get the file table data
		file_table: list[list] = []
		
		permission_table = b""
		filetree_table = b""
		ptoffset = 0
		fttoffset = 0
		# Read the file table
		current_offset: int = 0
		total_blocks = 0

		if entries > 0:
			for i in range(entries):
				file_entry = struct.unpack(
					FILE_TABLE_ENTRY_FORMAT,
					file_table_data[current_offset : current_offset + 140],
				)
				file_table.append((file_entry[0], file_entry[1] + file_entry[2], file_entry[3], file_entry[4])
				current_offset += self.ftentrysize
				total_blocks += file_entry[3]

		current_offset = 0
		temp_offset = 0
		index = 0
		old_block_span = 0
		block_span = 0

		# Check if the file already exists
		for entry in file_table:
			if entry[0] == file_name:
				# Overwrite
				current_offset = entry[1]
				old_block_span = entry[2]
				temp_offset = entry[3]
				permission_table = data[temp_offset:self.permissiontsize]
				p = struct.unpack(PERMISSION_TABLE_ENTRY_FORMAT, permission_table)
				
				writen = False
				
				if not writen:
					filetree_table = struct.unpack(FILE_TREE_ENTRY, data[p[1]:self.ftreeentrysize])
					if not caller == filetree_table[0].strip(b"\x00"):
						return -2200
						
					filetree_table = None
					permission_table = None
					p = None
				break
			index += 1
		else: # New file
			if not dummy:
				out = self.check_free_block(data[file_table_offset+len(file_table)*140:], ((len(file_data) + self.super_block.block_size - 1) // self.super_block.block_size))
				p = struct.unpack(PERMISSION_TABLE_ENTRY_FORMAT, file_table[len(file_table) - 1][3])
				if out is None:
					current_offset = file_table[len(file_table) - 1][1] + file_table[len(file_table) - 1][2] * self.super_block.block_size if file_table else 0
				else:
					current_offset = out
				
				ptoffset = file_table[len(file_table) - 1][3] + self.permissiontsize
				ftoffset = p[1] + self.ftreeentrysize
				p = None
				
				pcode = 0x0
				for permission in permissions:
					if isinstance(permission, list):
						break
						
					if permissions[0] == permission:
						pcode = permission
						continue
						
					pcode = pcode | permssion
				
				permission_table = struct.pack(PERMISSION_TABLE_ENTRY_FORMAT, pcode, ftoffset)
				
				if isinstance(permissions[len(permissions) - 1], list):
					if permissions[len(permissions) - 1] is None:
						pass
					else:
						file_entry_table = struct.pack(FILE_TREE_ENTRY_FORMAT, *e for e in permissions[len(permissions) - 1])
				
				old_block_span  = (len(file_data) + self.super_block.block_size - 1) // self.super_block.block_size
			else:
				current_offset = self.dummy_offset
				old_block_span = 0
			
			file_table.append((file_name, current_offset, old_block_span, temp_offset))
			entries += 1 # Increment file count
			total_blocks += old_block_span  # Update total block size

		current_offset = current_offset + file_table_offset + file_table.__len__() * 140

		if not dummy:
			block_span  = (len(file_data) + self.super_block.block_size - 1) // self.super_block.block_size
		else:
			block_span = 0

		if total_blocks > self.super_block.total_blocks:
			next_free_block = self.check_free_block(current_offset, data)
			if next_free_block is not None:
				current_offset = next_free_block
			else:
				# No free block found, expand the drive data file
				if not self.free_blocks:
					return -221  # No free blocks available, cannot expand the drive data file (1)
				else:
					data_t = data[old_block_span * self.super_block.block_size + file_table[index][1]:]  # Get the temp file data
					for i in range(old_block_span, block_span):
						if not self.free_blocks:
							break
						data_t = b'\x00' * self.super_block.block_size + data_t  # Add a new block of zeros to the data
						self.free_blocks.pop(len(self.free_blocks) - 1) # Remove the last free block

					data = data[:old_block_span * self.super_block.block_size + file_table[index][1]] + data_t + self.free_blocks.__len__() * self.super_block.block_size  # Update the data with the new blocks

		# **Handle block expansion**
		if block_span > old_block_span:
			next_free_block = self.check_free_block(current_offset, data)
			if next_free_block is not None:
				current_offset = next_free_block
			else:
				# No free block found, expand the drive data file
				if not self.free_blocks:
					return -222  # No free blocks available, cannot expand the drive data file
				else:
					data_t = data[old_block_span * self.super_block.block_size + file_table[index][1]:]  # Get the temp file data
					for i in range(old_block_span, block_span):
						if not self.free_blocks:
							break
						data_t = b'\x00' * self.super_block.block_size + data_t  # Add a new block of zeros to the data
						self.free_blocks.pop(len(self.free_blocks) - 1) # Remove the last free block

					data = data[:old_block_span * self.super_block.block_size + file_table[index][1]] + data_t + self.free_blocks.__len__() * self.super_block.block_size  # Update the data with the new blocks

		if block_span < old_block_span:
			# Remove data
			dt = b"\x00" * old_block_span * self.superblock.block_size

		# Update file table
		file_table_data = b''.join([struct.pack(FILE_TABLE_ENTRY_FORMAT, entry[0], int(str(entry[1])[:self.ftoffset1s]), int(str(entry[1])[self.ftoffset2s:]), entry[2]) for entry in file_table])

		# Make new header with new entries
		self.super_block.entries = entries
		self.super_block.file_table_offset = self.headersize + self.permissiontsize + self.freeentrysize + self.filetsize
		header = self.super_block.to_bytes()
		# Write the new header to the data
		updated_data = (
			header +
			
			file_table_data +
			data[file_table_offset + len(file_table_data) : file_table_offset + len(file_table_data) + file_table[index][1]] +  # Data before the file data
			file_data +  # File data
			data[file_table_offset + len(file_table_data) + file_table[index][1] + block_span * self.super_block.block_size:]  # Data after the file data
		)

		with open(self.drive_data_path, "wb") as f:
			f.seek(0)
			f.write(updated_data)  # Write the updated data

		self.files.append(file_name.strip(b"\x00").decode("utf-8"))  # Add the file name to the list of files

		return 0

	def get_file(self, file_name: bytes, size:int=None) -> bytes:
		"""Reads a file from the drive data file."""
		data:bytes = None
		try:
			with open(self.drive_data_path, "rb") as f:
				f.seek(0)
				data = f.read()

		except FileNotFoundError:
			init_vdrive(False, True)
			return None  # Return None if the file does not exist

		if file_name.decode("utf-8") in self.files:
			pass
		else:
			return None

		self.super_block.from_bytes(data[:struct.calcsize(PBFS_HEADER_FORMAT)])  # Read the superblock from the first 68 bytes
		file_table_offset = self.super_block.file_table_offset
		entries = self.super_block.entries
		file_offset:int = 0
		block_span:int = 0

		co = 0

		file_table_data = data[file_table_offset:]  # Read file table
		for i in range(entries):
			file_entry = struct.unpack(FILE_TABLE_ENTRY_FORMAT, file_table_data[co : co + 140])
			if file_entry[0].strip(b'\x00') == file_name:
				file_offset = file_entry[1]
				block_span = file_entry[2]
				if file_offset == self.dummy_offset:
					data = b"THIS IS A DUMMY FILE, IT HAS NO DATA!"  # Dummy file, no data
				else:
					data = data[file_offset + entries * 140 + file_offset : file_offset + entries * 140 + file_offset + block_span * self.super_block.block_size]  # Return the file data
			co += 140
		else:
			data = None

		if file_offset == self.dummy_offset and block_span == 0:
			return b""

		if data is not None:
			if size is None:
				return data

			if size > 0 and len(data) >= size:
				return data[:size]
			elif size > 0 and len(data) < size:
				return data + b'\x00' * (size - len(data))
			elif size <= 0:
				return None
			else:
				return data

		return None  # File not found

	def remove_file(self, file_name: bytes) -> int:
		"""Removes a file from the drive data file."""
		
		return self.write_file(file_name, b"\x00")
		
	def reload(self) -> None:
		# Just reload the drive data from the file
		data = ""

		try:
			with open(self.drive_data_path, "rb") as f:
				f.seek(0)
				data = f.read()

		except FileNotFoundError:
			init_vdrive(False, True)
			if not os.path.exists(self.drive_data_path):
				return
			self.reload()

		self.super_block.from_bytes(data[:68])  # Read the superblock from the first 68 bytes

		# Open the file meta data and store all files in self.files
		self.files.clear()
		ftoffset = self.super_block.file_table_offset
		entries = self.super_block.entries

		file_table_data = data[ftoffset:ftoffset + entries*140]  # Read file table

		for i in range(entries):
			file_entry = struct.unpack(
				FILE_TABLE_ENTRY_FORMAT,
				file_table_data[i * 140 : i * 140 + 140],
			)

			if file_entry[1] == self.dummy_offset:
				if file_entry[0].strip(b'\x00').decode("utf-8") == "__dir_marker__":
					self.dirs.append(file_entry[0].strip(b'\x00').decode("utf-8"))
					continue  # Skip dummy files
			self.files.append(file_entry[0].strip(b'\x00').decode("utf-8"))

		return

	def list_dir(self, dir: str = "") -> list[str]:
		"""Lists all files in the drive data file."""
		if not self.files:
			self.reload()
		if not self.files:
			return []

		result: set[str] = set()
		normalized_dir = ""
		if not dir == "" and dir is not None:
			normalized_dir = dir.strip("\\/")  # Normalize the directory path

		for file in self.files:
			parts = file.strip("\\/").split("\\") # Split path components
			if normalized_dir == "":
				if len(parts) == 1:
					result.add(parts[0]) # Just the file
				else:
					result.add(parts[0]) # Top level dir
			else:
				# inside a subdir
				dir_parts = normalized_dir.split("\\")
				if parts[:len(dir_parts)] == dir_parts:
					# Match the dir
					remaining_parts = parts[len(dir_parts):]
					if len(remaining_parts) == 1:
						# It's a file directly inside the dir
						result.add(remaining_parts[0])
					elif len(remaining_parts) > 1:
						# It's a file deeper inside a subdir, add the next dir
						result.add(remaining_parts[0])

		return sorted(result)  # Return sorted list of files

	def mk_dir(self, dirpath: bytes = b"") -> int:
		"""Creates a directory in the drive data file."""
		if not dirpath:
			return -224

		dir_str = dirpath.decode("utf-8").strip("\\/")

		if dir_str in self.dirs:
			return -225

		# Dummy file to mark the directory
		dummy_marker = b"__dir_marker__"
		out = self.write_file(self.join_path(dirpath, b"__dir_marker__"), b"")

		if out == 0:
			self.dirs.append(dir_str)

		return out

	def rm_dir(self, dirpath: bytes = b"", debug:bool=False) -> int:
		"""Removes a directory from the drive data file."""
		if not dirpath:
			return -226

		dir_str = dirpath.decode("utf-8").strip("\\/")
		dirpath = dir_str.encode("utf-8")

		if not dir_str in self.dirs:
			print(self.dirs)
			return -227

		# Remove all files in the directory
		for i, file in enumerate(self.files):
			if file.startswith(dir_str):
				# file
				if debug: print(f"Removing file: {file}")
				out = self.remove_file(file.encode("utf-8"))
				if out != 0:
					return out
				if debug: print(f"Removed file: {file}")
				self.files.pop(i)
				if "__dir_marker__" in file:
					self.dirs.remove(file.replace("__dir_marker__", "").strip("\\/"))

		self.reload()
		return 0

	def join_path(self, *args: bytes) -> bytes:
		"""Joins multiple path components into a single path."""
		parts = [arg.strip(b"\\/") for arg in args if arg]
		return b"\\".join(parts)

	def mv_dir(self, src: bytes, dst: bytes) -> int:
		"""Moves a directory from src to dst."""
		if not src or not dst:
			return -229

		src_str = src.decode("utf-8").strip("\\/")
		dst_str = dst.decode("utf-8").strip("\\/")

		if src_str not in self.dirs:
			return -230

		if dst_str in self.dirs:
			return -231

		out = self.mk_dir(dst)
		if out != 0:
			return out

		files = self.list_dir(src_str)
		for file in files:
			file_path = self.join_path(src, file.encode("utf-8"))
			data = self.get_file(file_path)
			out = self.remove_file(file_path)
			if out != 0:
				return out
			out = self.write_file(self.join_path(dst, file.encode("utf-8")), data)
			if out != 0:
				return out

		out = self.rm_dir(src)
		return out

	def dir_exists(self, dir: bytes) -> bool:
		"""Checks if a directory exists in the drive data file."""
		dir_str = dir.decode("utf-8").strip("\\/")
		out = False

		if dir_str in self.dirs:
			out = True
			return out

		# Try to get the file with the directory marker
		out_i = self.get_file(self.join_path(dir, b"__dir_marker__"))
		if out_i is not None:
			out = True
			self.dirs.append(dir_str)  # Add the directory to the list if it exists
		else:
			out = False

		return out

def init_vdrive(resetDrive: bool = False, reset_drive_data:bool = False, reset_superblock:bool = False) -> None:
	superblock = PBFS_SuperBlock()
	make_superblock = reset_superblock
	make_drive_data = reset_drive_data

	if not os.path.exists(DISK_PATH):
		make_superblock = True

	if not os.path.exists(os.path.join(base_path, ".hard_disk", "drive_data.pbfs")):
		make_drive_data = True

	if resetDrive:
		make_superblock = True
		make_drive_data = True

	if make_superblock:
		uuid_pbfs = uuid.uuid4().bytes
		drive_data_path = os.path.join(base_path, ".hard_disk", "drive_data.pbfs")
		data: bytes = bytearray()
		# Add all drive details here
		data += struct.pack("<I", superblock.block_size)  # Block size
		data += struct.pack("<I", superblock.total_blocks)  # Total blocks
		data += DISK_NAME
		data += struct.pack("<Q", superblock.timestamp)  # Timestamp
		data += struct.pack("<I", PBFS_VERSION)  # Version
		data += struct.pack("<Q", First_boot_timestamp)  # First boot timestamp
		data += struct.pack("<H", OS_boot_mode)  # OS boot mode
		data += uuid_pbfs  # UUID

		with open(DISK_PATH, "wb") as f:
			f.write(data)

		# Set the str representation of the OS boot mode
		if OS_boot_mode == 0:
			OS_boot_mode_str = "Potato Mode"
		elif OS_boot_mode == 1:
			OS_boot_mode_str = "Full Mode"
		elif OS_boot_mode == 2:
			OS_boot_mode_str = "Recovery Mode"
		else:
			OS_boot_mode_str = "Unknown Mode"

		# Prints
		print("Virtual Drive initialized:")
		print(f"\tBlock size: {superblock.block_size} bytes")
		print(f"\tTotal blocks: {superblock.total_blocks}")
		print(f"\tDisk name: {DISK_NAME}")
		print(f"\tTimestamp: {superblock.timestamp}")
		print(f"\tPBFS version: {PBFS_VERSION}")
		print(f"\tFirst boot timestamp: {First_boot_timestamp}")
		print(f"\tOS boot mode: {OS_boot_mode_str}")
		print(f"\tUUID: {uuid_pbfs}")

	if make_drive_data:
		readme:str = """README for PBFS Virtual Drive

		The structure of the PBFS virtual drive is as follows:
		[PBFS Header] -> Contains all the metadata about the drive
		[File Table] -> Contains all file names and their offsets
		 - Each file entry is 140 bytes long, with the first 128 bytes being the file name, the next 4 bytes being the file offset, and the last 8 bytes being the file data block span.
		[File Data] -> Contains the actual file data, padded to the nearest block size

		The PBFS virtual drive is a simple/complex file system made specifically for Python hence the name PBFS (Python Based File System). It is designed to be used with the PENV (Python Environment) of PHardwareITK (Python Hardware IT Kit) and is not meant to be used as a general-purpose file system outside of Python.
		The PBFS virtual drive is a single file that contains all the data of the virtual drive, including the metadata, file table, and file data. The PBFS virtual drive is not meant to be modified directly by users, but rather through the provided API.
		The OS files are not a part of the PBFS virtual drive to prevent users from modifying them directly, though the OS can if they want add the files to the drive data file using the provided API, but changing the code inside the virtual drive directly will not change OS behaviour.

		Created by Pheonix Studios -> Akshobhya Sasun (Founder/Creator of PHardwareITK and PheonixAppAPI family).
		"""

		drive_data = PBFS_DriveData()

		drive_data.write_base_data()  # Write the base data to the drive data file
		drive_data.write_file(b"vdrive.pbfs", b"This file is the virtual drive data file, users are not allowed to modify it directly or read it, hence this message when you opened it!") # Write a dummy file to the drive data file just for show
		drive_data.write_file(b"README_PBFS.txt", readme.encode("utf-8"))  # Write a readme file to the drive data file
		drive_data.reload()

		print("PBFS virtual disk (drive_data) created!")

def start(resetDrive: bool = False) -> None:
	"""Starts the PBFS virtual disk setup."""
	if not os.path.exists(os.path.join(base_path, ".hard_disk")):
		os.mkdir(os.path.join(base_path, ".hard_disk"))
	init_vdrive(resetDrive)

if __name__ == "__main__":
	if not os.path.exists(os.path.join(base_path, ".hard_disk")):
		os.mkdir(os.path.join(base_path, ".hard_disk"))

	if len(sys.argv) > 2:
		if sys.argv[1] == "reset":
			start(resetDrive=True)
		else:
			start()
	else:
		start()
