import os
import sys
import time
import struct

# NOTE: This is PBFS 64-bit version, for 128-bit version that supports ~356,000,000 Yottabytes please download the C/ASM version of pbfs! thanks a lot.
MPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if not MPATH in sys.path:
    sys.path.append(MPATH)

from Extensions import C
from Extensions.C import stdlib
from Extensions.C import stdio
from Extensions.C import stdint

PBFS_HEADER = {
    "Magic": {"type": C.array, "array_type": C.char, "array_len": 6, "value": None},
    "Block_Size": {"type": stdint.uint32_t, "value": None},
    "Total_Blocks": {"type": stdint.uint32_t, "value": None},
    "Disk_Name": {"type": C.array, "array_type": C.char, "array_len": 24, "value": None},
    "TimeStamp": {"type": stdint.uint64_t, "value": None},
    "Version": {"type": stdint.uint32_t, "value": None},
    "First_Boot_Timestamp": {"type": stdint.uint64_t, "value": None},
    "OS_BootMode": {"type": stdint.uint16_t, "value": None},
    "Entries": {"type": stdint.uint32_t, "value": None},
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
    "Name": {"type": C.array, "array_type": C.char, "array_len": 150, "value": None},
    "File_Data_Offset": {"type": stdint.uint64_t, "value": None},
    "Permission_Table_Offset": {"type": stdint.uint64_t, "value": None},
    "Block_Span": {"type": stdint.uint64_t, "value": None},
}

"""typedef struct {
	char Name[150]; // Name of the file
	uint64_t File_Data_Offset; // File data offset
	uint64_t Permission_Table_Offset; // Permission table offset
	uint64_t Block_Span; // File Block Span
} __attribute__((packed)) PBFS_FileTableEntry; // Total = 24 bytes"""

PBFS_PERMISSION_TABLE_ENTRY = {
    "Read": {"type": stdint.uint16_t, "value": None},
    "Write": {"type": stdint.uint16_t, "value": None},
    "Executable": {"type": stdint.uint16_t, "value": None},
    "Listable": {"type": stdint.uint16_t, "value": None},
    "Hidden": {"type": stdint.uint16_t, "value": None},
    "Full_Control": {"type": stdint.uint16_t, "value": None},
    "Delete": {"type": stdint.uint16_t, "value": None},
    "Special_Access": {"type": stdint.uint16_t, "value": None},
    "File_Tree_Offset": {"type": stdint.uint32_t, "value": None},
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
    "Name": {"type": C.array, "array_type": C.char, "array_len": 20, "value": None}
}

"""typedef struct {
	char Name[20]; // Name of the file (unique id is also accepted, it is 20 bytes because the file paths are not used here but rather the unique id is used).
} __attribute__((packed)) PBFS_FileTreeEntry; // Total = 20 bytes"""

PBFS_DAP = {
    "size": {"type": stdint.uint8_t, "value": None},
    "reserved": {"type": stdint.uint8_t, "value": None},
    "sector_count": {"type": stdint.uint16_t, "value": None},
    "offset": {"type": stdint.uint16_t, "value": None},
    "segment": {"type": stdint.uint16_t, "value": None},
    "lba": {"type": stdint.uint64_t, "value": None},
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
    "Read": {"type": stdint.uint16_t, "value": None},
    "Write": {"type": stdint.uint16_t, "value": None},
    "Executable": {"type": stdint.uint16_t, "value": None},
    "Listable": {"type": stdint.uint16_t, "value": None},
    "Hidden": {"type": stdint.uint16_t, "value": None},
    "Full_Control": {"type": stdint.uint16_t, "value": None},
    "Delete": {"type": stdint.uint16_t, "value": None},
    "Special_Access": {"type": stdint.uint16_t, "value": None},
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
    "Header_Start": {"type": stdint.uint64_t, "value": None},
    "Header_End": {"type": stdint.uint64_t, "value": None},
    "Header_BlockSpan": {"type": stdint.uint64_t, "value": None},
    "Bitmap_Start": {"type": stdint.uint64_t, "value": None},
    "Bitmap_BlockSpan": {"type": stdint.uint64_t, "value": None},
    "Bitmap_End": {"type": stdint.uint64_t, "value": None},
    "Data_Start": {"type": stdint.uint64_t, "value": None},
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
    "size": {"type": stdint.uint16_t, "value": None},
    "flags": {"type": stdint.uint16_t, "value": None},
    "cylinders": {"type": stdint.uint32_t, "value": None},
    "heads": {"type": stdint.uint32_t, "value": None},
    "sectors_per_track": {"type": stdint.uint32_t, "value": None},
    "total_sectors": {"type": stdint.uint64_t, "value": None},
    "bytes_per_sector": {"type": stdint.uint16_t, "value": None},
    "reserved": {"type": C.array, "array_type": stdint.uint8_t, "array_len": 6, "value": None},
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
    "Name": {"type": C.pointer, "ptr_type": C.char, "value": None},
    "lba": {"type": stdint.uint64_t, "value": None},
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
    C.push_frame()
    if not os.path.exists(path):
        return False

    drive: C.pointer[stdio.FILE] = stdio.fopen(path, "rb")
    stdio.fseek(drive, C.Int(0), C.Int(stdio.SEEK_END))
    size = stdio.ftell(drive)
    stdio.fseek(drive, C.Int(0), C.Int(stdio.SEEK_SET))
    buffer_ = stdlib.malloc(C.size_t(block_size))
    buffer_.cast(C.Char)
    stdio.fseek(drive, C.Int(block_size), C.Int(stdio.SEEK_SET))
    stdio.fread(buffer_, C.size_t(block_size), C.size_t(1), drive)
    err = C.struct.from_address(PBFS_HEADER, buffer_.ptr_addr)
    if err == -1:
        print("Incorrect data in file: Validation Failed!")
        stdlib.free(buffer_)
        stdio.fclose(drive)
        C.pop_frame()
        return False

    magic = err.Magic
    magic_val = C.pointer(magic.address, C.char).deref()
    if not magic_val == b"PBFS\x00\x00":
        print("Signature doesn't Match! Validation failed!")
        stdlib.free(buffer_)
        stdio.fclose(drive)
        C.pop_frame()
        return False

    stdlib.free(buffer_)
    stdio.fclose(drive)
    C.pop_frame()
    return True

def format_disk(
    path: str,
    total_blocks: int = 2048,
    block_size: int = 512,
    disk_name: bytes = b"SSD-PBFS-VIRTUAL",
) -> int:
    """Formates the Drive"""
    C.reset_mem(memsize) # Always ensure clean slate
    C.push_frame()
    print("Formatting disk...")
    file: C.pointer[stdio.FILE] = stdio.fopen(path, "wb+")

    if isinstance(file, C.Int):
        print("Opening the file failed:", file)
        return -1

    try:
        lba_buff = stdlib.malloc(C.size_t(block_size))
        if not lba_buff: 
            print("Alloc failed!")
            return -1
        # Now we format it
        print("Formatting...")
        C.write_mem(b"\x00" * block_size, block_size, lba_buff.ptr_addr)
        stdio.fwrite(lba_buff, C.size_t(block_size), C.size_t(1), file)

        print("Writing PBFS Header...")
        PBFS_Header = C.struct.from_address(PBFS_HEADER, lba_buff.ptr_addr)
        PBFS_Header.Magic = b"PBFS\x00\x00"
        PBFS_Header.Block_Size = stdint.uint32_t(block_size)
        PBFS_Header.Total_Blocks = stdint.uint32_t(total_blocks)
        PBFS_Header.Disk_Name = disk_name
        PBFS_Header.TimeStamp = stdint.uint64_t(int(time.time()))
        PBFS_Header.Version = stdint.uint32_t(1)
        PBFS_Header.Entries = stdint.uint32_t(0)
        PBFS_Header.First_Boot_Timestamp = stdint.uint64_t(0)
        PBFS_Header.OS_BootMode = stdint.uint16_t(1)

        print("lba addr: ", lba_buff.ptr_addr)

        print("Writing...")
        stdio.fwrite(lba_buff, C.size_t(block_size), C.size_t(1), file)
        C.write_mem(b"\x00" * block_size, block_size, lba_buff.ptr_addr)
        
        # Create bitmap
        print("Creating Bitmap")
        
        def make_bitmap(total_blocks_, reserved_blocks=3):
            bytes_needed = (total_blocks_ + 7) // 8
            bitmap = bytearray(bytes_needed)
            
            for block in range(reserved_blocks):
                byte_index = block // 8
                bit_index = block % 8
                bitmap[byte_index] |= (1 << bit_index)
                
            return bitmap
        
        bmap = make_bitmap(total_blocks, 3)
        space_needed = (total_blocks + 7) // 8
        
        C.write_mem(bmap, space_needed, lba_buff.ptr_addr)
        stdio.fwrite(lba_buff, C.size_t(block_size), C.size_t(space_needed), file)
        
        stdio.fwrite(b"\x00" * block_size, C.size_t(block_size), C.size_t(total_blocks - (1 + space_needed)), file)
        
        print("Done formatting disk...")
        stdio.fflush(file)
    except Exception as e:
        print(f"Exception: {e}")
        stdio.fclose(file)
        stdlib.free(lba_buff)
        print("FAILED!")
        C.pop_frame()
        return -1
    stdio.fclose(file)
    stdlib.free(lba_buff)

    print("Finished!")
    C.pop_frame()

    return 0


def increase_memsize(size_: int):
    """Increase the default memory size for this file"""
    global memsize
    memsize = size_
    C.reset_mem(size_)

def initialize_pbfs(size_: int):
    global memsize
    memsize = size_
    C.initialize(size_)


class PBFS:
    """Python Block File System / Pheonix Block File System"""

    def __init__(self, drive: str, block_size: int=512, total_blocks: int=2048) -> None:
        pass