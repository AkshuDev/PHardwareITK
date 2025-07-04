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
	"Magic": {
		"type": Pointer[Char],
		"value": None
	},

	"Block_Size": {
		"type": Uint32_t,
		"value": None
	},
	"Total_Blocks": {
		"type": Uint32_t,
		"value": None
	},
	"Disk_Name": {
		"type": Pointer[Char],
		"value": None
	},
	"TimeStamp": {
		"type": Uint64_t,
		"value": None
	},
	"Version": {
		"type": Uint32_t,
		"value": None
	},
	"First_Boot_Timestamp": {
		"type": Uint64_t,
		"value": None
	},
	"OS_BootMode": {
		"type": Uint16_t,
		"value": None
	},
	"Entries": {
		"type": Uint32_t,
		"value": None
	}
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
	"Name": {
		"type": Array[Char, 128],
		"value": None
	},
	"File_Data_Offset": {
		"type": Uint64_t,
		"value": None
	},
	"Permission_Table_Offset": {
		"type": Uint64_t,
		"value": None
	},
	"Block_Span": {
		"type": Uint64_t,
		"value": None
	}
}

"""typedef struct {
	char Name[128]; // Name of the file
	uint64_t File_Data_Offset; // File data offset
	uint64_t Permission_Table_Offset; // Permission table offset
	uint64_t Block_Span; // File Block Span
} __attribute__((packed)) PBFS_FileTableEntry; // Total = 152 bytes"""

PBFS_PERMISSION_TABLE_ENTRY = {
	"Read": {
		"type": Uint16_t,
		"value": None
	},
	"Write": {
		"type": Uint16_t,
		"value": None
	},
	"Executable": {
		"type": Uint16_t,
		"value": None
	},
	"Listable": {
		"type": Uint16_t,
		"value": None
	},
	"Hidden": {
		"type": Uint16_t,
		"value": None
	},
	"Full_Control": {
		"type": Uint16_t,
		"value": None
	},
	"Delete": {
		"type": Uint16_t,
		"value": None
	},
	"Special_Access": {
		"type": Uint16_t,
		"value": None
	},
	"File_Tree_Offset": {
		"type": Uint32_t,
		"value": None
	}
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
	"Name": {
		"type": Array[Char, 20],
		"value": None
	}
}

"""typedef struct {
	char Name[20]; // Name of the file (unique id is also accepted, it is 20 bytes because the file paths are not used here but rather the unique id is used).
} __attribute__((packed)) PBFS_FileTreeEntry; // Total = 20 bytes"""

PBFS_DAP = {
	"size": {
		"type": Uint8_t,
		"value": None
	},
	"reserved": {
		"type": Uint8_t,
		"value": None
	},
	"sector_count": {
		"type": Uint16_t,
		"value": None
	},
	"offset": {
		"type": Uint16_t,
		"value": None
	},
	"segment": {
		"type": Uint16_t,
		"value": None
	},
	"lba": {
		"type": Uint64_t,
		"value": None
	}
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
	"Read": {
		"type": Uint16_t,
		"value": None
	},
	"Write": {
		"type": Uint16_t,
		"value": None
	},
	"Executable": {
		"type": Uint16_t,
		"value": None
	},
	"Listable": {
		"type": Uint16_t,
		"value": None
	},
	"Hidden": {
		"type": Uint16_t,
		"value": None
	},
	"Full_Control": {
		"type": Uint16_t,
		"value": None
	},
	"Delete": {
		"type": Uint16_t,
		"value": None
	},
	"Special_Access": {
		"type": Uint16_t,
		"value": None
	}
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
	"Header_Start": {
		"type": Uint64_t,
		"value": None
	},
	"Header_End": {
		"type": Uint64_t,
		"value": None
	},
	"Header_BlockSpan": {
		"type": Uint64_t,
		"value": None
	},
	"Bitmap_Start": {
		"type": Uint64_t,
		"value": None
	},
	"Bitmap_BlockSpan": {
		"type": Uint64_t,
		"value": None
	},
	"Bitmap_End": {
		"type": Uint64_t,
		"value": None
	},
	"Data_Start": {
		"type": Uint64_t,
		"value": None
	}
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
	"size": {
		"type": Uint16_t,
		"value": None
	},
	"flags": {
		"type": Uint16_t,
		"value": None
	},
	"cylinders": {
		"type": Uint32_t,
		"value": None
	},
	"heads": {
		"type": Uint32_t,
		"value": None
	},
	"sectors_per_track": {
		"type": Uint32_t,
		"value": None
	},
	"total_sectors": {
		"type": Uint64_t,
		"value": None
	},
	"bytes_per_sector": {
		"type": Uint16_t,
		"value": None
	},
	"reserved": {
		"type": Array[Uint8_t, 6],
		"value": None
	}
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
	"Name": {
		"type": Pointer[Char],
		"value": None
	},
	"lba": {
		"type": Uint64_t,
		"value": None
	}
}

"""typedef struct {
	char* name;
	uint64_t lba;
} PBFS_FileListEntry;"""

def format_disk(path:str, total_blocks:int=2048, block_size:int=512, disk_name:bytes=b'SSD-PBFS-VIRTUAL') -> int:
	print("Formatting disk...")
	path = make_string(path)
	mode = make_string("wb+")
	file:Pointer[FILE] = fopen(path, mode)

	# Now we format it
	PBFS_Header = Struct(PBFS_HEADER)
	PBFS_Header.set("Magic", make_string("PBFS\x00\x00"))
	PBFS_Header.set("Block_Size", Uint32_t(block_size))
	PBFS_Header.set("Total_Blocks", Uint32_t(total_blocks))
	PBFS_Header.set("Disk_Name", make_string(disk_name))
	PBFS_Header.set("Timestamp", Uint64_t(int(time.time())))
	PBFS_Header.set("Version", Uint32_t(1))
	PBFS_Header.set("Entries", Uint32_t(0))

	print("Writing PBFS Header...")
	lba1_buff = malloc(block_size)

	PBFS_Header.write_b(lba1_buff)

	print("Writing PBFS Header to file...")
	print(f"Writing - \n{read(lba1_buff, block_size)}")
	fwrite("\x00", 1, block_size, file)
	fseek(file, block_size + 1, SEEK_SET)
	fwrite(lba1_buff, block_size, 1, file)

	free(lba1_buff)
	print("Done formatting disk...")
	fclose(file)

	print("Finished!")

	return 0

