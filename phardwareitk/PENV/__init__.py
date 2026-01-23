"""DO NOT USE YET!

PENV stands for Pheonix Environment, it is a full virtual machine requiring no dependencies, it is capable of loading multiple OS made in either .py (python) or .vasm (Virtual Assembly). (NOTE: Learn more about .vasm from PVCpu)

It has a BIOS, it is capable of loading a 512-byte or less .vasm/.py file with AA55 signature. If it is a .py file it is run in complete restriction and can call the BIOS via -
```python
__int__(code:int)
```

PENV also has GUI capabilites and Driver support.

PENV provides AOS:PENV by default, it is an OS that uses CLI and can run .aosf (AOS Executable File) and .caosf (Compressed AOS Executable File).

You can upgrade to AOS++:PENV for free but it will use more resources. It will provide GUI support and even Extension support.
"""

import os
import sys
import subprocess
import math
import json

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
module_path = os.path.join(base_path, "..", "..")

if module_path not in sys.path:
    sys.path.insert(0, module_path)

from phardwareitk.Memory import Memory as memory
from phardwareitk.PENV.shared import *

win32, posix, unknown, os_ = get_os()

PENV_DISK = os.path.join(base_path, "PheonixSSD.penv")

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

def copy_folder_to_disk(folder_path: str, block_size: int = 512, total_blocks: int = 2048):
    """
    Recursively copies a files into Drive.
    
    Args:
        folder_path (str): Path to the folder to copy.
        block_size (int, optional): Size of a single block. Defaults to 512 bytes.
        total_blocks (int, optional): Total block in the entire drive. Defaults to 2048
    """
    
    # Normalize folder path
    folder_path = os.path.abspath(folder_path)
    total_disk_blocks = 0
    excluded_dirs = []
    
    with open(PENV_DISK, "wb") as disk:
        for root, dirs, files_ in os.walk(folder_path):
            files = []
            if root in excluded_dirs:
                continue
            
            if "penv_info.json" in files_:
                files_.remove("penv_info.json")
                data = {}
                with open(os.path.join(root, "penv_info.json"), "r") as pinfo:
                    data = json.load(pinfo)
                if data.get("min_req_blocks", total_blocks) > total_blocks:
                    return None
                if data.get("exclude", None):
                    for ex in data["exclude"]:
                        if ex.endswith("/*"):
                            dirs = os.listdir(root)
                            for d in dirs:
                                if os.path.isdir(os.path.join(root, d)) and d == ex.replace("/*", ""):
                                    excluded_dirs.append(os.path.join(root, d))
                        elif ex in files_:
                            files_.remove(ex)
                if data.get("order", None):
                    for ofile, order in data["order"].items():
                        if ofile in files_:
                            files_.remove(ofile)
                            lba: int = -1
                            if order.get("lba", None):
                                lba = order["lba"]
                            files.insert(order.get("idx", len(files) - 1), (ofile, lba))
                for f in files_:
                    files.append((f, -1))
            else:
                for f in files_:
                    files.append((f, -1))
                
            # Copy files
            for f, lba in files:
                abs_file_path = os.path.join(root, f)
                
                if lba > -1:
                    disk.seek(lba*block_size)
                
                # Read file content
                with open(abs_file_path, "r") as fd:
                    content = fd.read()
                    disk.write(content.encode("utf-8"))
                blocks_needed = math.ceil(len(content) / block_size)
                total_size = blocks_needed * block_size
                padding = total_size - len(content)
                disk.write(b'\0' * padding)
                total_disk_blocks += blocks_needed

        block_padding = total_blocks - total_disk_blocks
        if block_padding < 0:
            return None
        disk.write(b'\0'*block_size*block_padding)

def start_penv(
    max_ram_bytes: int = 2 * 1000000,
    process_ram_size: int = 1 * 1000000,
    command_py: str = "python",
    bheight: int = 500,
    bwidth: int = 800,
    bdepth: int = 3,
    total_blocks:int = 2048,
    disk_name: str = "PheonixSSD",
    include_uefi: bool = True,
    format_drive: bool = False,
    os: str = "" # Uses current OS
) -> None:
    """Starts Pheonix Virtual Environment"""
    from phardwareitk.PENV import bios
    
    block_size: int = 512
    
    if format_drive:
        print("Formatting the drive")
        with open(PENV_DISK, "wb") as disk:
            disk.write(b'\0'*total_blocks*block_size)
        bios.make_drive_info(block_size, total_blocks, disk_name, 0)
        print("Formatted!")
        sys.exit(0)
    
    if not os == "":
        print("Downloading OS...")
        copy_folder_to_disk(os, block_size, total_blocks)
        print("Downloaded OS...")
        sys.exit(0)
        
    bios.start(process_ram_size, 0)
    
if __name__ == "__main__":
    start_penv()
