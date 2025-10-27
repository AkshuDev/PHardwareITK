"""DO NOT USE YET!

PENV stands for Pheonix Environment, it is a full virtual machine requiring no dependencies, it is capable of loading multiple OS made in either .py (python) or .vasm (Virtual Assembly). (NOTE: Learn more about .vasm from PVCpu)

It has a BIOS, it is capable of loading a 512-byte or less .vasm/.py file with AA55 signature. If it is a .py file it is run in complete restriction and can call the BIOS via -
```python
__int__(code:int)
```

PENV also has GUI capabilites and Driver support. (NOTE: Currently remapping the entire FileSystem so please wait till it is ready!)

PENV provides AOS:PENV by default, it is an OS that uses CLI and can run .aosf (AOS Executable File) and .caosf (Compressed AOS Executable File).

You can upgrade to AOS++:PENV for free but it will use more resources. It will provide GUI support and even Extension support.
"""

import os
import sys
import subprocess

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
module_path = os.path.join(base_path, "..", "..")

if module_path not in sys.path:
    sys.path.insert(0, module_path)

from phardwareitk.Memory import Memory as memory
from phardwareitk.PENV.shared import *
from phardwareitk.Extensions.C import *
from phardwareitk.Extensions.C.stdlib import *
from phardwareitk.Extensions.C.stdio import *
from phardwareitk.Extensions.C.stdint import *

win32, posix, unknown, os_ = get_os()

PBFS_DISK = os.path.join(base_path, "PheonixSSD.pbfs")

def force_os(_os: str, posix_based_os: bool = False) -> None:
    """Forces a OS so that the script will follow that specific os

    Args:
            _os (str): The OS you want to force.
    """
    _os = _os.lower()

    if _os == "windows":
        win32 = True
        posix = False
        unknown = False
    elif _os in posix_os:
        posix = True
        unknown = False
        win32 = False
    else:
        os_ = _os
        unknown = False
        win32 = False
        posix = False
        if posix_based_os:
            posix = True

def copy_folder_to_pbfs(pbfs, folder_path: str, reserved_size: int = 0, permissions: tuple = (1,1,1,1,0,0,1,0)):
    """
    Recursively copies a folder into PBFS.
    
    Args:
        pbfs (PBFS): The mounted PBFS instance.
        folder_path (str): Path to the folder to copy.
        reserved_size (int): Extra space to reserve per file.
        permissions (tuple): Permissions to apply to all files.
    """
    
    # Normalize folder path
    folder_path = os.path.abspath(folder_path)
    base_name = os.path.basename(folder_path)
    
    for root, dirs, files in os.walk(folder_path):
        # Compute relative path inside the drive
        rel_root = os.path.relpath(root, folder_path)
        if rel_root == ".":
            rel_root = ""  # root folder itself
        
        # Create folder entries (optional, for hierarchical tree)
        for d in dirs:
            folder_rel_path = os.path.join(base_name, rel_root, d).replace("\\", "/")
            pbfs.make_meta_entry(folder_rel_path + "/", 0, 0, 0, dir_=True)
        
        # Copy files
        for f in files:
            file_rel_path = os.path.join(base_name, rel_root, f).replace("\\", "/")
            abs_file_path = os.path.join(root, f)
            
            # Read file content
            with open(abs_file_path, "rb") as fd:
                content = fd.read()
            
            # Write file into PBFS
            pbfs.write_file(content, file_rel_path, reserved_size=reserved_size, permissions=permissions)

def start_penv(
    max_ram_bytes: int = 2 * 1000000,
    process_ram_size: int = 1 * 1000000,
    command_py: str = "python",
    bheight: int = 500,
    bwidth: int = 800,
    bdepth: int = 3,
    total_blocks:int = 2048,
    block_size: int = 512,
    disk_name: str = "PheonixSSD",
    include_uefi: bool = True,
    format_drive: bool = False,
    os: str = "" # Uses current OS
) -> None:
    """Starts Pheonix Virtual Environment"""
    from phardwareitk.PENV import PBFS
    from phardwareitk.PENV import bios

    memsize_part = process_ram_size // 4

    initialize(memsize_part)
    PBFS.initialize_pbfs(memsize_part)

    cmem = get_memory()

    if PBFS.validate_disk(PBFS_DISK, block_size) == False or format_drive:
        print("Creating PBFS Disk...")
        err = PBFS.format_disk(PBFS_DISK, total_blocks, block_size, b"disk_name")
        if err < 0:
            sys.exit(err)
    
    fs = PBFS.PBFS(PBFS_DISK, block_size, total_blocks)
    
    if not os == "":
        print("Formatting Drive...")
        PBFS.format_disk(PBFS_DISK, total_blocks, block_size, b"disk_name")
        print("Downloading OS...")
        copy_folder_to_pbfs(fs, os)
        print("Downloaded OS...")
        sys.exit(0)
    
if __name__ == "__main__":
    start_penv()
