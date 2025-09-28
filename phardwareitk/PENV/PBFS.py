import os
import sys
import time
import struct

# NOTE: This is PBFS 64-bit version, for 128-bit version that supports ~356,000,000 Yottabytes please download the C/ASM version of pbfs! thanks a lot.
MPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if not MPATH in sys.path:
    sys.path.append(MPATH)

from Extensions.C import *
from Extensions.C_IO import *

PBFS_HEADER = {
    "Magic": {"type": Pointer, "ptr_type": Char, "value": None},
    "Block_Size": {"type": Uint32_t, "value": None},
    "Total_Blocks": {"type": Uint32_t, "value": None},
    "Disk_Name": {"type": Pointer, "ptr_type": Char, "value": None},
    "TimeStamp": {"type": Uint64_t, "value": None},
    "Version": {"type": Uint32_t, "value": None},
    "First_Boot_Timestamp": {"type": Uint64_t, "value": None},
    "OS_BootMode": {"type": Uint16_t, "value": None},
    "Entries": {"type": Uint32_t, "value": None},
}

"""typedef struct {
	char Magic[6]; // PBFS\x00\x00
	uint32_t Block_Size; // 512 bytes by default (BIOS BLOCK SIZE)
	uint32_t Total_Blocks;  // 2048 blocks for 1MB
	char Disk_Name[24]; // Just the name of the disk for the os
	uint64_t Timestamp; // Timestamp
	uint32_t Version; // Version
	uint64_t First_Boot_Timestamp; // First boot timestamp
	uint16_t OS_BootMode; // Again optional but there for furture use!
	uint32_t FileTableOffset; // Offset of the file table (first data block)
	uint32_t Entries; // Number of entries in the file table
} __attribute__((packed)) PBFS_Header; // Total = 68 bytes"""

PBFS_FILE_TABLE_ENTRY = {
    "Name": {"type": Pointer, "ptr_type": Char, "value": None},
    "File_Data_Offset": {"type": Uint64_t, "value": None},
    "Permission_Table_Offset": {"type": Uint64_t, "value": None},
    "Block_Span": {"type": Uint64_t, "value": None},
}

"""typedef struct {
	char* Name; // Name of the file
	uint64_t File_Data_Offset; // File data offset
	uint64_t Permission_Table_Offset; // Permission table offset
	uint64_t Block_Span; // File Block Span
} __attribute__((packed)) PBFS_FileTableEntry; // Total = 24 bytes"""

PBFS_PERMISSION_TABLE_ENTRY = {
    "Read": {"type": Uint16_t, "value": None},
    "Write": {"type": Uint16_t, "value": None},
    "Executable": {"type": Uint16_t, "value": None},
    "Listable": {"type": Uint16_t, "value": None},
    "Hidden": {"type": Uint16_t, "value": None},
    "Full_Control": {"type": Uint16_t, "value": None},
    "Delete": {"type": Uint16_t, "value": None},
    "Special_Access": {"type": Uint16_t, "value": None},
    "File_Tree_Offset": {"type": Uint32_t, "value": None},
}

"""typedef struct {
	uint16_t Read; // Read Permission
	uint16_t Write; // Write Permission
	uint16_t Executable; // Executable Permission
	uint16_t Listable; // Listable Permission
	uint16_t Hidden; // Hidden Permission
	uint16_t Full_Control; // System File Permission
	uint16_t Delete; // Delete Permission
	uint16_t Special_Access; // Special Access
	uint32_t File_Tree_Offset; // Offset of the file tree
} __attribute__((packed)) PBFS_PermissionTableEntry; // Total = 20 bytes"""

PBFS_FILE_TREE_ENTRY = {
    "Name": {"type": Array, "array_type": Char, "array_size": 20, "value": None}
}

"""typedef struct {
	char Name[20]; // Name of the file (unique id is also accepted, it is 20 bytes because the file paths are not used here but rather the unique id is used).
} __attribute__((packed)) PBFS_FileTreeEntry; // Total = 20 bytes"""

PBFS_DAP = {
    "size": {"type": Uint8_t, "value": None},
    "reserved": {"type": Uint8_t, "value": None},
    "sector_count": {"type": Uint16_t, "value": None},
    "offset": {"type": Uint16_t, "value": None},
    "segment": {"type": Uint16_t, "value": None},
    "lba": {"type": Uint64_t, "value": None},
}

"""typedef struct {
	uint8_t size;
	uint8_t reserved;
	uint16_t sector_count;
	uint16_t offset;
	uint16_t segment;
	uint64_t lba;
} __attribute__((packed)) PBFS_DAP;"""

PBFS_PERMISSIONS = {
    "Read": {"type": Uint16_t, "value": None},
    "Write": {"type": Uint16_t, "value": None},
    "Executable": {"type": Uint16_t, "value": None},
    "Listable": {"type": Uint16_t, "value": None},
    "Hidden": {"type": Uint16_t, "value": None},
    "Full_Control": {"type": Uint16_t, "value": None},
    "Delete": {"type": Uint16_t, "value": None},
    "Special_Access": {"type": Uint16_t, "value": None},
}

"""typedef struct {
	uint16_t Read; // Read Permission
	uint16_t Write; // Write Permission
	uint16_t Executable; // Executable Permission
	uint16_t Listable; // Listable Permission
	uint16_t Hidden; // Hidden Permission
	uint16_t Full_Control; // System File Permission
	uint16_t Delete; // Delete Permission
	uint16_t Special_Access; // Special Access
} __attribute__((packed)) PBFS_Permissions; // Total = 16 bytes"""

PBFS_LAYOUT = {
    "Header_Start": {"type": Uint64_t, "value": None},
    "Header_End": {"type": Uint64_t, "value": None},
    "Header_BlockSpan": {"type": Uint64_t, "value": None},
    "Bitmap_Start": {"type": Uint64_t, "value": None},
    "Bitmap_BlockSpan": {"type": Uint64_t, "value": None},
    "Bitmap_End": {"type": Uint64_t, "value": None},
    "Data_Start": {"type": Uint64_t, "value": None},
}

"""typedef struct {
	uint64_t Header_Start;
	uint64_t Header_End;
	uint64_t Header_BlockSpan;
	uint64_t Bitmap_Start;
	uint64_t Bitmap_BlockSpan;
	uint64_t Bitmap_End;
	uint64_t Data_Start;
} __attribute__((packed)) PBFS_Layout;"""

DRIVE_PARAMETERS = {
    "size": {"type": Uint16_t, "value": None},
    "flags": {"type": Uint16_t, "value": None},
    "cylinders": {"type": Uint32_t, "value": None},
    "heads": {"type": Uint32_t, "value": None},
    "sectors_per_track": {"type": Uint32_t, "value": None},
    "total_sectors": {"type": Uint64_t, "value": None},
    "bytes_per_sector": {"type": Uint16_t, "value": None},
    "reserved": {"type": Array[Uint8_t, 6], "value": None},
}

"""typedef struct {
	uint16_t size;              // 0x00 - Must be 0x1E (30)
	uint16_t flags;             // 0x02
	uint32_t cylinders;         // 0x04 - reserved or zero
	uint32_t heads;             // 0x08 - reserved or zero
	uint32_t sectors_per_track; // 0x0C - reserved or zero
	uint64_t total_sectors;     // 0x10 - important!
	uint16_t bytes_per_sector;  // 0x18 - important!
	uint8_t  reserved[6];       // 0x1A - reserved
} __attribute__((packed)) DriveParameters;"""

PBFS_FILE_LIST_ENTRY = {
    "Name": {"type": Pointer, "ptr_type": Char, "value": None},
    "lba": {"type": Uint64_t, "value": None},
}

"""typedef struct {
	char* name;
	uint64_t lba;
} PBFS_FileListEntry;"""

memsize = 64

def round_up_to_block(size: int, block_size: int = 512) -> int:
    return ((size + block_size - 1) // block_size) * block_size

def validate_disk(path: str, block_size: int = 512) -> bool:
    """Validates the Drive"""
    global size

    if not os.path.exists(path):
        return False

    path = make_string(path)
    mode = make_string("rb")

    drive: Pointer[FILE] = fopen(path, mode)
    PBFS_Header = Struct(PBFS_HEADER)
    fseek(drive, 0, SEEK_END)
    size = ftell(drive)
    fseek(drive, 0, SEEK_SET)
    buffer_ = malloc(block_size)
    buffer_.cast(Char)
    fseek(drive, block_size, SEEK_SET)
    fread(buffer_, block_size, 1, drive)
    err = PBFS_Header.fill_b(read(buffer_, size))
    if err == -1:
        print("Incorrect data in file: Validation Failed!")
        free(buffer_)
        fclose(drive)
        return False

    magic = PBFS_Header.access("Magic")
    magic_val = read(magic, 6)
    if not magic_val == b"PBFS\x00\x00":
        print("Signature doesn't Match! Validation failed!")
        free(buffer_)
        fclose(drive)
        return False

    free(buffer_)
    fclose(drive)
    return True

def format_disk(
    path: str,
    total_blocks: int = 2048,
    block_size: int = 512,
    disk_name: bytes = b"SSD-PBFS-VIRTUAL",
) -> int:
    """Formates the Drive"""
    print("Formatting disk...")
    path = make_string(path)
    mode = make_string("wb+")
    file: Pointer[FILE] = fopen(path, mode)

    # Now we format it
    PBFS_Header = Struct(PBFS_HEADER)
    PBFS_Header.set("Magic", make_string("PBFS\x00\x00"))
    PBFS_Header.set("Block_Size", Uint32_t(block_size))
    PBFS_Header.set("Total_Blocks", Uint32_t(total_blocks))
    PBFS_Header.set("Disk_Name", make_string(disk_name))
    PBFS_Header.set("TimeStamp", Uint64_t(int(time.time())))
    PBFS_Header.set("Version", Uint32_t(1))
    PBFS_Header.set("Entries", Uint32_t(0))
    PBFS_Header.set("First_Boot_Timestamp", Uint64_t(0))
    PBFS_Header.set("OS_BootMode", Uint16_t(1))

    print("Formatting...")
    lba_buff = malloc(block_size)
    write(lba_buff, b"\x00" * block_size, block_size, no_meta=True)
    fwrite(lba_buff, block_size, 1, file)

    err = PBFS_Header.write_b(lba_buff)
    if err < 0:
        print("Error Occured, Quitting!")
        return -1

    del PBFS_Header
    print("Writing PBFS Header...")
    fwrite(lba_buff, block_size, 1, file)
    write(lba_buff, b"\x00" * block_size, block_size, no_meta=True)
    
    # Create bitmap
    print("Creating Bitmap")
    write(lba_buff, b"\x01\x01\x01"+(b"\x00"*(block_size - 3)), block_size, no_meta=True)
    space_needed = round_up_to_block(total_blocks, block_size) // block_size
    fwrite(lba_buff, block_size, space_needed, file)
    write(lba_buff, b"\x00" * block_size, block_size, no_meta=True) # Cleanup
    
    blocks_left = total_blocks - (1 + 1 + space_needed)
    if blocks_left > 0:
        fwrite(lba_buff, block_size, blocks_left, file)
    
    print("Done formatting disk...")
    fflush(file)
    fclose(file)
    free(lba_buff)

    print("Finished!")

    return 0


def increase_memsize(size_: int):
    """Increase the default memory size for this file"""
    global size
    size = size_
    reset_mem(size)


class PBFS:
    """Python Block File System / Pheonix Block File System"""

    def __init__(self, drive: str, block_size: int=512, total_blocks: int=2048) -> None:
        self.drive = drive
        self.files = []
        self.folders = []
        
        self.block_size = block_size
        self.total_blocks = total_blocks
        
        self.layout = Struct(PBFS_LAYOUT)
        self.layout.set("Header_Start", Uint64_t(block_size))
        self.layout.set("Header_BlockSpan", Uint64_t(1))
        self.layout.set("Header_End", Uint64_t(block_size * 2))
        self.layout.set("Bitmap_Start", Uint64_t(block_size * 2))
        
        self.header = Struct(PBFS_HEADER)
        
        self.drive_file = fopen(make_string(self.drive), make_string("rb+"))
        
        self.read_header()
        
        # Initialize bitmap
        self.bitmap = bytearray
        self.load_bitmap()
        self.list_files()
        
    def validate_header(self) -> bool:
        """Validates the header"""
        magic = self.header.access("Magic")
        if read(magic, 6) == b"PBFS\x00\x00":
            return True
        return False
        
    def read_header(self) -> bool:
        """Reads the header"""
        fseek(self.drive_file, self.layout.access("Header_Start").value, SEEK_SET)
        data = malloc(self.layout.access("Header_BlockSpan").value * self.block_size)
        fread(data, self.layout.access("Header_BlockSpan").value * self.block_size, 1, self.drive_file)
        self.header.fill_b(read(data, self.layout.access("Header_BlockSpan").value * self.block_size))
        
        if not self.validate_header():
            return False
        
        self.block_size = self.header.access("Block_Size").value
        self.total_blocks = self.header.access("Total_Blocks").value
        
        bm_blockspan = round_up_to_block(self.total_blocks, self.block_size) // self.block_size
        bm_end = self.layout.access("Bitmap_Start").value + (bm_blockspan * self.block_size)
        
        self.layout.set("Bitmap_BlockSpan", Uint64_t(bm_blockspan))
        self.layout.set("Bitmap_End", Uint64_t(bm_end))
        self.layout.set("Data_Start", Uint64_t(bm_end + (2 * self.block_size)))

    def is_block_free(self, block_index: int) -> bool:
        """Checks if the specified block is free"""
        if self.bitmap[block_index] == b"\x00":
            return True
        elif self.bitmap[block_index] == b"\x01":
            return False
        else:
            print(f"BITMAP IS MALFORMED!, GOT {self.bitmap[block_index]}")
            raise Exception(f"BITMAP IS MALFORMED!, GOT {self.bitmap[block_index]}")
    
    def mark_blocks_used(self, start_block: int, count: int):
        """Marks a block used"""
        self.bitmap[start_block] = b"\x01"
        for i in range(count):
            self.bitmap[start_block + i] = b"\x01"
    
    def mark_blocks_free(self, start_block: int, count: int):
        """Marks a block free"""
        self.bitmap[start_block] = b"\x00"
        for i in range(count):
            self.bitmap[start_block + 1] = b"\x00"

    def get_free_blocks(self, span: int) -> int:
        """Return starting block index of 'span' free blocks or -1 if none"""
        free_count = 0
        start_block = 0
    
        for block in range(self.total_blocks):
            if self.is_block_free(block):
                if free_count == 0:
                    start_block = block
                free_count += 1
                if free_count == span:
                    return start_block
            else:
                free_count = 0

        return -1  # no free continuous range found

    def write_file(self, content: bytes, path: str, reserved_size:int=0, permissions:tuple=(1, 1, 0, 1, 0, 0, 1, 0), files_with_access:list=["~"]) -> bool:
        """Write a file to Drive

        Parameters:
            content (bytes): The content of the file
            path (str): Path of the file
            reserved_size (int): Extra space if needed to reserve. Defaults to 0

        Returns:
            bool: True if successful else False"""
        
        size = len(content) + reserved_size
        extra_size = round_up_to_block(size, self.block_size)
        path += "\x00\x00"
        
        if not size == extra_size:
            content += b"\x00" * extra_size
            size = extra_size
            
        block_span = size // self.block_size
        addr = self.get_free_blocks(block_span + 1)
        if addr == -1:
            print("No Space Left on Device")
            return False
            
        addr = addr * self.block_size
        fseek(self.drive_file, addr + self.block_size, SEEK_SET)
        data = malloc(size)
        write(data, content, size, no_meta=True)
        fwrite(data, size, 1, self.drive_file)
        free(data)
        tree = self.make_file_tree(files_with_access)
        perm = self.make_permission_table(*permissions, addr + 44)
        meta = self.make_meta_entry(path, addr + self.block_size, block_span, addr + 24, False)
        
        lba_buff = malloc(self.block_size)
        meta.write_b(lba_buff)
        perm.write_b(Pointer(Void, lba_buff.pointer_address + 24))
        write(Pointer(Void, lba_buff.pointer_address + 44), tree, len(tree))
        fseek(self.drive_file, addr, SEEK_SET)
        fwrite(lba_buff, self.block_size, 1, self.drive_file)
        free(lba_buff)
        del meta
        del perm
        return True
        
    def list_files(self) -> dict:
        """
        Returns a hierarchical dict of files/folders and updates self.files/self.folders.
        Example:
        {
            "folder1": {
                "file1.txt": {...},
                "subfolder": {
                    "file2.txt": {...}
                }
            },
            "file3.txt": {...}
        }
        """
        self.files = []
        self.folders = []
    
        def add_to_tree(tree: dict, path_parts: list, meta: Struct):
            part = path_parts.pop(0)
            if len(path_parts) == 0:
                # leaf node = file
                tree[part] = {"meta": meta}
            else:
                if part not in tree:
                    tree[part] = {}
                add_to_tree(tree[part], path_parts, meta)
    
        file_tree: dict = {}
        # Loop over all blocks containing metadata
        data_start = self.layout.access("Data_Start").value
        for block in range(self.total_blocks):
            if not self.is_block_free(block):
                # Read the metadata block
                offset = block * self.block_size
                buf = malloc(self.block_size)
                fseek(self.drive_file, offset, SEEK_SET)
                fread(buf, self.block_size, 1, self.drive_file)
                meta_block = Struct(PBFS_FILE_TABLE_ENTRY)
                meta_block.fill_b(read(buf, self.block_size))
    
                # Only process valid entries
                name_bytes = meta_block.access("Name")
                path_str = read(name_bytes, 20).rstrip(b"\x00").decode("utf-8")
                if not path_str:
                    continue
    
                # Update self.files/self.folders
                entry = {
                    "path": path_str,
                    "addr": meta_block.access("File_Data_Offset").value,
                    "span": meta_block.access("Block_Span").value
                }
                self.files.append(entry)
    
                # Build hierarchical dict
                path_parts = path_str.split("/")
                add_to_tree(file_tree, path_parts, meta_block)

        return file_tree
        
    def load_bitmap(self) -> None:
        """Reads the bitmap from disk into memory"""
        bm_start = self.layout.access("Bitmap_Start").value
        bm_size_bytes = self.total_blocks
        buf = malloc(bm_size_bytes)
        
        fseek(self.drive_file, bm_start, SEEK_SET)
        fread(buf, bm_size_bytes, 1, self.drive_file)
        data = read(buf, bm_size_bytes)
        self.bitmap = bytearray(data)
        free(buf)
            
    def make_meta_entry(self, path:str, addr:int, block_span:int, permission_table_offset:int, dir_:bool=False) -> Struct:
        """Creates and returns a File Table Entry"""
        entry = {"path": path, "addr": addr, "span": block_span, "permission_table_offset": permission_table_offset}
        if dir_:
            self.folders.append(entry)
        else:
            self.files.append(entry)
            
        meta_entry = Struct(PBFS_FILE_TABLE_ENTRY)
        meta_entry.set("Name", make_string(path))
        meta_entry.set("File_Data_Offset", Uint64_t(addr))
        meta_entry.set("Permission_Table_Offset", Uint64_t(permission_table_offset))
        meta_entry.set("Block_Span", Uint64_t(block_span))
        
        return meta_entry
        
    def make_permission_table(read:int, write:int, executable:int, listable:int, hidden:int, full_control:int, delete:int, special_access:int, file_tree_offset:int) -> Struct:
        """Creates and returns the permission table"""
        permissions = Struct(PBFS_PERMISSION_TABLE_ENTRY)
        permissions.set("Read", Uint16_t(read))
        permissions.set("Write", Uint16_t(write))
        permissions.set("Executable", Uint16_t(executable))
        permissions.set("Listable", Uint16_t(listable))
        permissions.set("Hidden", Uint16_t(hidden))
        permissions.set("Full_Control", Uint16_t(full_control))
        permissions.set("Special_Access", Uint16_t(special_access))
        permissions.set("File_Tree_Offset", Uint32_t(file_trr_offset))
        
        return permissions
        
    def make_file_tree(files:list=["~"]) -> bytes:
        """Creates and returns the file tree"""
        tree:bytes = b""
        for file in files:
            file = file.encode("utf-8")
            size = len(file)
            if size > 20:
                return tree
            elif size < 20:
                file += b"\x00" * (20 - size)
            
            tree += file
            
        return tree
        
    def read_file(self, path: str) -> bytes:
        """Read a file from the drive by its path"""
        # Find the file entry
        entry = None
        for f in self.files:
            if f["path"].rstrip("\x00") == path:
                entry = f
                break
    
        if entry is None:
            raise FileNotFoundError(f"File '{path}' not found in PBFS.")
    
        offset = entry["addr"]
        block_span = entry["span"]
        size = block_span * self.block_size
    
        # Allocate buffer and read from disk
        buf = malloc(size)
        fseek(self.drive_file, offset, SEEK_SET)
        fread(buf, size, 1, self.drive_file)
        data = read(buf, size)
        free(buf)
    
        # Trim any padding zeros that were added during write
        data = data.rstrip(b"\x00")
        return data
    
    def close_drive(self) -> None:
        """Closes the drive and frees up all the memory"""
        del self.header
        del self.layout
        fclose(self.drive)
        return
    