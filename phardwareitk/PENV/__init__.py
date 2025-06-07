import os
import sys
import subprocess

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
module_path = os.path.join(base_path, "..")

if not module_path in sys.path:
    sys.path.append(module_path)

from phardwareitk.Memory import Memory as memory
from phardwareitk.PENV.shared import *

win32, posix, unknown, os_ = get_os()

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
) -> None:
    """Starts Pheonix Virtual Environment"""
    from phardwareitk.PENV import PBFS
    from phardwareitk.PENV import bios
    from phardwareitk.PENV import framebuffer as FrameBuffer_mi

    # Set framebuffer
    fb = FrameBuffer_mi.Framebuffer

    PBFS.start()
    # File System Done
    # Start BIOS stage 1
    filename_bootloader = bios.start()
    # Set up Memory and ram
    mem = memory.Memory(520, 0)
    # Start Bios stage 2
    table_, sys_data, drive_data, drive_path = bios.run_bootloader(
        filename_bootloader, mem, 65, fb
    )

    if not isinstance(table_, str) or table_ == "!ERROR!":
        mem = None
        return

    # Check execution
    table_ = json.loads(table_)
    type_ = table_["type"]
    fname = table_["filename"]
    args = None

    if ddh_key(table_, "args"):
        args = table_["args"]

    # Set globals for shared
    set_disk_data(drive_data)
    set_sys_data(sys_data)

    set_framebuffer(fb)

    while type_ == 0x60:
        # Stage 2 is called probably
        # Clean bootloader/file from mem
        mem.write_ram(b"\x00", 65, 520)
        # Write stage 2
        sz = os.stat(os.path.join(drive_path, fname)).st_size
        if sz > 512:
            return

        set_mem(mem)

        exec_globals = {}
        exec_globals["__int__"] = interrupt

        with open(os.path.join(drive_path, fname), "rb") as f:
            mem.write_ram(f.read(), 65)

        try:
            exec(mem.get_ram(sz, 65), exec_globals)
        except Exception as e:
            table_ = json.loads(str(e))
            fname = table_["filename"]
            type_ = table_["type"]

    args = None
    if ddh_key(table_, "args"):
        args = table_["args"]

    if not type_ == 0x51:
        return

    import gc

    # Cleanup mem
    set_mem(None)
    mem.ram = bytearray(1)
    mem = None
    gc.collect()
    # Create mem path for kernel
    mem = os.path.join(module_path, "Memory")
    # Create Display table
    display_table = {
        "vga": None,
        "framebuffer": [bwidth, bheight, bdepth],
        "display_path": os.path.join(module_path, "PENV"),
    }
    # Set args
    subproc_args = [
        mem,
        str(max_ram_bytes),
        str(process_ram_size),
        json.dumps(display_table),
        str(base_path)
    ]
    if args:
        for i in args:
            if isinstance(i, int):
                i = str(i)
            elif isinstance(i, dict):
                i = json.dumps(i)
            subproc_args.append(i)
    args = None

    #Close framebuffer here
    try:
        fb.delete()
    except TypeError:
        pass
    fb = None
    gc.collect()

    # Call
    return subprocess.run(
        [command_py, os.path.join(drive_path, fname), *subproc_args],
        shell=False,
        capture_output=False,
        text=False,
    )
