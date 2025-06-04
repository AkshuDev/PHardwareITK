import os
import sys
import time
import struct
import uuid
from typing import *

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
    "<HHHHHHHHI" # Permissions in int (8 bytes), File Names tree entry offset (4 bytes), Total = 12 bytes
)

FILE_TREE_ENTRY_FORMAT: str = (
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

        self.header_size:int = struct.calcsize(PBFS_HEADER_FORMAT) # Size of the PBFS header in bytes
        self.file_table_entry_size:int = struct.calcsize(FILE_TABLE_ENTRY_FORMAT)  # Size of each file table entry in bytes
        self.permission_table_entry_size:int = struct.calcsize(PERMISSION_TABLE_ENTRY_FORMAT)  # Size of each permission table entry in bytes
        self.file_tree_entry_size:int = struct.calcsize(FILE_TREE_ENTRY_FORMAT)  # Size of each file tree entry in bytes
        # Total per entry = 296 bytes
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

    def check_free_blocks(self, offset: int, data: bytes, blocks_span_to_search:int) -> int:
        """Finds a number of consecutive free blocks in data."""

        # Check for consecutive number of free blocks in data
        block_size = self.super_block.block_size
        total_bytes_needed = blocks_span_to_search * block_size

        data = data[offset:]  # Start from the given offset

        for i in range(0, len(data) - total_bytes_needed + 1, block_size):
            span = data[i:i + total_bytes_needed]
            if span == b'\x00' * total_bytes_needed:
                # Found consecutive free blocks
                return offset + i

        return None  # No sufficient span of free blocks found

    def file_table_handler(self, offset: int, data: bytes, write: bool = False, entries: int=0, file_name: bytes=b"", file_data_offset: int=0, block_span: int=0, permission_offset: int=0) -> Union[list, bytes]:
        """Handles the file table in the drive data file."""
        # Read the file table from the drive data file
        file_table_data = b""
        file_table = []

        if not write:
            # We have to read the file table and return it
            file_table_data = data[offset:self.file_table_entry_size] # Get file table data
            for entry in range(entries):
                file_entry = struct.unpack(
                    FILE_TABLE_ENTRY_FORMAT,
                    file_table_data[entry * self.file_table_entry_size : (entry + 1) * self.file_table_entry_size],
                )
                file_table.append(file_entry)

            return file_table  # Return the file table as a list of tuples
        else:
            # We have to write the file table entry to the drive data file
            file_table_data = struct.pack(
                FILE_TABLE_ENTRY_FORMAT,
                file_name.ljust(128, b'\x00'),  # File name padded to 128 bytes
                file_data_offset,  # File offset part 1
                block_span,  # File offset part 2
                permission_offset,  # Permission Table Offset
                entries,  # Total entries in the file table
            )
            return file_table_data

    def permission_table_handler(self, offset: int, data: bytes, write: bool = False, entries:int=0, permissions:list=[0x0, 0x1], file_tree_offset: int=0) -> Union[list, bytes]:
        """Handles the permission table in the drive data file."""
        # Read the permission table from the drive data file
        permission_table_data = b""
        permission_table = []

        if not write:
            # We have to read the permission table and return it
            permission_table_data = data[offset:self.permission_table_entry_size]
            for entry in range(entries):
                permission_entry = struct.unpack(
                    PERMISSION_TABLE_ENTRY_FORMAT,
                    permission_table_data[entry * self.permission_table_entry_size : (entry + 1) * self.permission_table_entry_size],
                )
                permission_table.append(permission_entry)

            return permission_table  # Return the permission table as a list of tuples
        else:
            p0 = 0
            p1 = 0
            p2 = 0
            p3 = 0
            p4 = 0
            p5 = 0
            p6 = 0
            p7 = 0

            for perm in permissions:
                if perm == 0x0:
                    p0 = 1
                elif perm == 0x1:
                    p1 = 1
                elif perm == 0x2:
                    p2 = 1
                elif perm == 0x3:
                    p3 = 1
                elif perm == 0x4:
                    p4 = 1
                elif perm == 0x5:
                    p5 = 1
                elif perm == 0x6:
                    p6 = 1
                elif perm == 0x7:
                    p7 = 1

            # We have to write the permission table entry to the drive data file
            permission_table_data = struct.pack(
                PERMISSION_TABLE_ENTRY_FORMAT,
                p0, # Permission Read
                p1, # Permission Write
                p2, # Permission Execute
                p3, # Permission Delete (Requires admin or OS permission to delete)
                p4, # Permission Rename
                p5, # Permission Hidden
                p6, # Permission List
                p7, # Permission Change Permissions
                file_tree_offset,  # File Names tree entry offset
            )
            return permission_table_data

    def file_tree_handler(self, offset:int, data:bytes, write:bool=False, file_names:list[bytes]=[b""]) -> Union[list, bytes]:
        """Handles the file tree in the drive data file."""
        # Read the file tree from the drive data file
        file_tree_data = b""
        file_tree = []

        if not write:
            # We have to read the file tree and return it
            file_tree_data = data[offset:]

            # Loop from the entry with not '.' as the start it denotes the root node then continue all the files till one of the file doens't have '.' which means that all the files inside the root node are read
            end = False

            while not end:
                file_entry = struct.unpack(
                    FILE_TREE_ENTRY_FORMAT,
                    file_tree_data[:self.file_tree_entry_size],
                )
                if file_entry[0].strip(b'\x00') == b"~":
                    # add the root node
                    file_tree_data = file_tree_data[self.file_tree_entry_size:]
                    file_tree.append(file_entry[0].strip(b'\x00').strip(b"~").decode("utf-8")) # we need to add root node
                    continue
                elif not file_entry[0].strip(b'\x00') == b".":
                    # End of the file tree
                    end = True
                    break
                elif file_entry[0].strip(b'\x00') == b".":
                    file_tree.append(file_entry[0].strip(b'\x00').decode("utf-8"))

            return file_tree
        else:
            # We have to write the file tree entry to the drive data file
            for file in file_names:
                if not isinstance(file, bytes):
                    file = file.encode("utf-8")

                if file == file_names[0]:
                    # Add the root node
                    file_tree.append(b"~"+file)
                else:
                    file_tree.append(b"."+file)

            file_tree_data = struct.pack(
                FILE_TREE_ENTRY_FORMAT,
                b"".join(file_tree).ljust(self.file_tree_entry_size, b'\x00'),  # File names padded to 128 bytes
            )

            return file_tree_data  # Return the file tree data as bytes

    def write_file(self, file_name: bytes, file_data: bytes, permissions:list=[0x0, 0x1, [None]]) -> int:
        """Writes a file to the drive data file."""
        # Structure ->
        # [PBFS Header] -> Contains all the metadata about the drive
        # [File Table] -> Contains all file names and their offsets
        # [File Data] -> Contains the actual file data
        # Check if file headers are present
        if not os.path.exists(self.drive_data_path):
            init_vdrive(False, True)
            return -220

        if not file_name or not file_data:
            return -221

        if not isinstance(file_name, bytes):
            file_name = file_name.encode("utf-8")
        if not isinstance(file_data, bytes):
            file_data = file_data.encode("utf-8")

        # Pad the file name and file data
        file_name = file_name.ljust(128, b'\x00')  # Pad file name to 128 bytes
        file_data = self.pad_data(file_data)

        # Read the drive data file
        data: bytes = b""
        try:
            with open(self.drive_data_path, "rb") as f:
                f.seek(0)
                data = f.read()
        except FileNotFoundError:
            init_vdrive(False, True)
            return -222

        # Set up self.superblock
        self.super_block.from_bytes(data[:struct.calcsize(PBFS_HEADER_FORMAT)])  # Read the superblock from the first 68 bytes
        file_table_offset = self.super_block.file_table_offset
        entries = self.super_block.entries
        current_offset = 0
        permission_offset = 0
        file_tree_offset = 0
        file_data_offset = 0
        block_span = 0
        total_block_span = 0

        file_table = []
        permission_table = []
        file_tree = []

        permission_table_data = b""
        file_tree_data = b""

        # Make Permissions list without the files list inside it and add the file names to the file tree list
        file_tree_list = [permissions[len(permissions) - 1]] if len(permissions) > 0 and isinstance(permissions[len(permissions) - 1], list) else [None]  # Last element is the file names list
        permissions.pop(len(permissions) - 1)

        # Read the file Table
        file_table_data = data[file_table_offset:]  # Read file table
        file_table = self.file_table_handler(file_table_offset, data, False, entries)  # Get the file table as a list of tuples

        # Check if the file already exists
        for file_entry in file_table:
            if file_entry[0].strip(b'\x00') == file_name:
                # File already exists, update the file data
                file_data_offset = (file_entry[1] << 32) | file_entry[2]
                block_span = file_entry[3]
                permission_offset = file_entry[4]
                total_block_span += block_span
                break
        else:
            # File does not exist, create a new entry
            # Calculate the block span needed for the file data
            block_span = (len(file_data) + self.super_block.block_size - 1) // self.super_block.block_size
            total_block_span += block_span

            file_data_offset = self.check_free_blocks(file_table_offset + entries * self.file_table_entry_size + self.header_size, data, block_span)
            if file_data_offset is None:
                # No free block found, return error
                return -223

            # Set the permission table offset to the last permission entry offset + permission entry size
            permission_offset = file_table[len(file_table) - 1][4] + self.permission_table_entry_size if len(file_table) > 0 else file_table_offset + entries * self.file_table_entry_size
            # set file Tree offset
            file_tree_offset = permission_offset + self.permission_table_entry_size  # File tree offset is after the permission table index 0
            # Set permission data
            permission_table_data = self.permission_table_handler(permission_offset, data, True, entries, permissions, file_tree_offset)
            # Set file tree data
            file_tree_data = self.file_tree_handler(file_tree_offset, data, True, file_tree_list if file_tree_list[0] is not None else [b"~"])  # Add the root node to the file tree

            # Split the file data offset into 2 parts, part 1, 4 bytes and part 2, 4 bytes
            mask_4bytes = 0xFFFFFFFF  # Mask for 4 bytes

            low = file_data_offset & mask_4bytes  # Low 4 bytes
            high = (file_data_offset >> 32) & mask_4bytes  # High 4 bytes

            # Add the new file entry to the file table
            file_table.append(
                (
                    file_name,  # File name
                    high,  # File offset part 1
                    low,  # File offset part 2
                    block_span,  # Block Span
                    permission_offset,  # Permission Table Offset
                )
            )

            entries += 1

        file_table_data = self.file_table_handler(file_table_offset, data, True, entries, file_name, file_data_offset, block_span, permission_offset)  # Write the file table entry to the drive data file

        # Read the permission table and add the new permission entry
        permission_table_data = self.permission_table_handler(file_table_offset + entries * self.file_table_entry_size, data, False, entries) + permission_table_data
        # Same with the file tree
        file_tree_data = self.file_tree_handler(file_tree_offset, data, False, file_tree_list) + file_tree_data

        # check if the total block span exceeds the max
        if total_block_span > self.super_block.total_blocks:
            return -224

        # Write the file data to the drive data file
        # New header
        self.super_block.entries = entries
        header = self.super_block.to_bytes()

        updated_data = (
            header +
            file_table_data + # File table data
            permission_table_data +  # Permission table data
            file_tree_data +  # File tree data
            data[file_table_offset + len(file_table_data) + len(permission_table_data) + len(file_tree_data):file_data_offset] + # Data before file data
            file_data + # File Data
            data[file_table_offset + len(file_table_data) + len(permission_table_data) + len(file_tree_data) + file_data_offset + (block_span * self.super_block.block_size):] # Data after file data
        )

        # Write Data
        with open(self.drive_data_path, "wb") as f:
            f.write(updated_data)

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

        self.reload()

        i = 0

        # We get the file from file table

        file_table = self.file_table_handler(self.super_block.file_table_offset, data, False, self.super_block.entries)

        for index, entry in file_table:
            if entry[0].strip(b"\x00") == file_name:
                i = index
                break
        else:
            return None

        permission_table = self.permission_table_handler(file_table[i][4], data, False, self.super_block.entries)

        if permission_table[0] == 1:
            file_data = data[self.super_block.file_table_offset + self.super_block.entries * self.file_table_entry_size + ((file_table[i][1] << 32) | file_table[i][2]):file_table[i][3]]
            if size is not None:
                file_data = file_data[:size]

            return file_data

        file_tree = self.file_tree_handler(permission_table[8], data, False)

        if not self.get_caller() in file_tree:
            return -230

        file_data = data[self.super_block.file_table_offset + self.super_block.entries * self.file_table_entry_size + ((file_table[i][1] << 32) | file_table[i][2]):file_table[i][3]]
        if size is not None:
            file_data = file_data[:size]

        return file_data

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
