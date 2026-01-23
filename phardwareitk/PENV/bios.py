import os
import sys
import json
import uuid
from datetime import datetime, timezone
import platform
from . import *
from . import Devices as devices

if not module_path in sys.path:
    sys.path.append(module_path)

if not os.path.dirname(__file__) in sys.path:
    sys.path.append(os.path.dirname(__file__))

from phardwareitk.Memory import Memory as Mem
from phardwareitk.PENV.shared import *

SystemData: dict = {}
drive_data: dict = {}

DRIVE_PATH = os.path.join(base_path, "PheonixSSD.penv")
VINFO_PATH = os.path.join(base_path, "vdrive.info")

# Get System Info
def GetSystemInfoBIOS(drive_info: dict, memsize: int) -> None:
    """Gets System Info"""
    
    SystemData["cpu_cores"] = int(os.cpu_count())
    SystemData["cpu_architecture"] = str(platform.machine())
    SystemData["processor_name"] = str(platform.processor())
    SystemData["host_name"] = str(platform.node())
    SystemData["host_system"] = str(platform.system())
    SystemData["host_version"] = str(platform.version())
    SystemData["host_release"] = str(platform.release())
    SystemData["host_platform"] = str(platform.platform())
    SystemData["host_uname"] = str(platform.uname())
    SystemData["storage_size"] = drive_info.get("block_size", 512) * drive_info.get("total_blocks", 2048) # in Bytes
    SystemData["ram_size"] = memsize # in bytes
    
def make_drive_info(block_size: int, total_blocks: int, disk_name: str, boot_mode: int):
    info = {
        "disk_name": disk_name,
        "block_size": block_size,
        "total_blocks": total_blocks,
        "boot_mode": boot_mode,
        "first_boot_timestamp": 0,
        "timestamp": int(datetime.now(timezone.utc).timestamp()),
        "uuid": str(uuid.uuid4())
    }
    
    with open(VINFO_PATH, "w") as f:
        json.dump(info, f)

def get_drive_data() -> int:
    if not os.path.exists(DRIVE_PATH):
        return -1  # Drive Error

    if not os.path.exists(VINFO_PATH):
        return -2  # Drive Info Not Found

    with open(VINFO_PATH, "r") as f:
        data = f.read()
    drive_data_ = json.loads(data)

    return drive_data_
    
def reset_timestamp(which_ts: int):
    ts = int(datetime.now(timezone.utc).timestamp())
    drive_info = get_drive_data()
    if not isinstance(drive_info, dict):
        return None
    try:
        if which_ts in [1, 3]:
            # Default Timestamp
            drive_info["timestamp"] = ts
        if which_ts in [2, 3]:
            drive_info["first_boot_timestamp"] = ts
            
        with open(VINFO_PATH, "w") as f:
            json.dump(drive_info, f)
    except Exception:
        return None

def search_for_bootloader() -> str:
    """Searches for the bootloader in the drive."""
    
    vinfo = get_drive_data()
    if not isinstance(vinfo, dict):
        return "", 0
    bootloader = ""
    bl_max_size = vinfo.get("block_size", 512)

    # Search the first block:
    with open(DRIVE_PATH, "rb") as f:
        bootloader = f.read(bl_max_size).strip(b'\0').decode("utf-8")
        buff = bootloader[-4:]
        if buff == "AA55":
            pass
        elif buff == "A55\n": #Incase of auto newline
            buff = bootloader[-5:]
            if buff == b"AA55\n":
                pass
            else:
                bootloader = ""
        else:
            bootloader = ""
        
    if not bootloader:
        print("No bootloader found. Please install a bootloader.")
        return "", 0

    return bootloader, len(bootloader)

def run_bootloader(mem: Mem.Memory, general_ram_start_addr: int, memsize: int) -> tuple:
    set_mem(mem)
    bl, bl_size = search_for_bootloader()
    mem.write_ram(bl.encode("utf-8"), general_ram_start_addr)

    _drive_data = get_drive_data()
    if not isinstance(_drive_data, dict):
        return None
    set_disk_data(_drive_data)
    set_sys_data(GetSystemInfoBIOS(_drive_data, memsize))

    exec_globals = {}
    exec_globals["__int__"] = interrupt
    exec_globals["__builtins__"] = {}

    print("Running Bootloader...")
    try:
        exec(mem.get_ram(bl_size, general_ram_start_addr).decode("utf-8"), exec_globals, None)
    except PenvInturruptReturn as e:
        if _drive_data["first_boot_timestamp"] == 0:
            # Write the timestamp to the drive data
            reset_timestamp(2)

            print("Updated first boot timestamp")

        return (str(e), SystemData, _drive_data, DRIVE_PATH)

def start(base_size: int, general_ram_addr: int) -> str:
    mem = Mem.Memory(base_size, 0, None, False, 0)
    status = run_bootloader(mem, general_ram_addr, base_size)
    if status:
        se, sysd, drived, drivep = status
        e = json.loads(se)
        etype = e.get("type", -1)
        if etype == 0x51: # Protected Mode
            # Run kernel
            esize = e.get("size", 0)
            elba = e.get("lba", 1)
            eloc = elba * drived.get("block_size", 512)
            kernel = ""
            with open(drivep, "rb") as f:
                f.seek(eloc)
                for i in range(esize):
                    kernel += f.read(drived.get("block_size", 512)).strip(b'\0').decode("utf-8")
            exec_globals = {}
            exec_globals["__system_info__"] = sysd
            exec_globals["__drive_info__"] = drived
            exec_globals["__drive_path__"] = drivep
            exec_globals["__args__"] = e.get("kernel_args", None)
            exec_globals["__in__"] = devices.route_in
            exec_globals["__out__"] = devices.route_out
            exec_globals["__builtins__"] = {}
            exec(kernel, exec_globals, None)
