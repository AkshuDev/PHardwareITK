import os
import sys
import subprocess

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
module_path = os.path.join(base_path, "..")

if not module_path in sys.path:
    sys.path.append(module_path)

from phardwareitk.Memory import Memory as memory
from phardwareitk.PENV.shared import *
from phardwareitk.Extensions.C import *
from phardwareitk.Extensions.C_IO import *

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
    include_uefi: bool = False,
) -> None:
    """Starts Pheonix Virtual Environment"""
    from phardwareitk.PENV import PBFS
    from phardwareitk.PENV import bios

    reset_mem(process_ram_size, debug=True)

    cmem = get_memory()

    if not os.path.exists(PBFS_DISK):
        print("Creating PBFS Disk...")
        PBFS.format_disk(PBFS_DISK, total_blocks, block_size, disk_name)


