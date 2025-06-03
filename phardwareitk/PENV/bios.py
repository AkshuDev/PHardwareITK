import os
import sys
import struct
from . import *

if not module_path in sys.path:
    sys.path.append(module_path)

from phardwareitk.Memory import Memory as memory
from phardwareitk.PENV.shared import *
from phardwareitk.PENV.framebuffer import Framebuffer
from phardwareitk.PENV import PBFS

SystemData: dict = {}
drive_data: dict = {}

DRIVE_PATH = os.path.join(base_path, ".hard_disk")

# Get System Info
def GetSystemInfoBIOS() -> None:
    """Gets System Info"""
    import psutil

    SystemData["cpu_cores"] = os.cpu_count()
    SystemData["cpu_architecture"] = platform.machine()
    SystemData["processor_name"] = platform.processor()
    SystemData["host_name"] = platform.node()
    SystemData["host_system"] = platform.system()
    SystemData["host_version"] = platform.version()
    SystemData["host_release"] = platform.release()
    SystemData["host_platform"] = platform.platform()
    SystemData["host_uname"] = platform.uname()
    SystemData["ram_size"] = round(
        psutil.virtual_memory().total / (1024**3), 2
    )  # in GB
    SystemData["storage_size"] = round(
        psutil.disk_usage("/").total / (1024**3), 2
    )  # in GB

def get_drive_data() -> int:
    if not os.path.exists(DRIVE_PATH):
        return -1  # Drive Error

    if not os.path.exists(os.path.join(DRIVE_PATH, "vdrive.pbfs")):
        return -2  # Drive Not Found

    if not os.path.exists(os.path.join(DRIVE_PATH, "drive_data.pbfs")):
        return -3  # Drive Data Not Found

    with open(os.path.join(DRIVE_PATH, "vdrive.pbfs"), "rb") as f:
        data = f.read()
    drive_data = struct.unpack("<II24sQIQH", data[:54])
    drive_data_ = {}
    drive_data_["block_size"] = drive_data[0]
    drive_data_["total_blocks"] = drive_data[1]
    drive_data_["disk_name"] = drive_data[2].decode("utf-8").strip("\x00")
    drive_data_["timestamp"] = drive_data[3]
    drive_data_["version"] = drive_data[4]
    drive_data_["first_boot_timestamp"] = drive_data[5]
    drive_data_["os_boot_mode"] = drive_data[6]
    return drive_data_

def search_for_bootloader() -> str:
    """Searches for the bootloader in the drive data directory."""
    # search the directory for file -> boot.info
    bootinfo_path = os.path.join(DRIVE_PATH, "boot.info")
    bootinfo_found: bool = True
    bootloader_path = ""
    if not os.path.exists(bootinfo_path):
        bootinfo_found = False

    # IF oot Info file is not found, it means this is a first time boot
    if not bootinfo_found:
        # Search the dir for all .py files
        files = []

        for file_ in os.listdir(DRIVE_PATH):
            if file_.endswith(".py"):
                files.append(file_)

        if not files:
            # Search all 512-byte files
            for file_ in os.listdir(DRIVE_PATH):
                if os.stat(os.path.join(DRIVE_PATH, file_)).st_size == 512:
                    files.append(file_)

        print("Acceptable maybe bootloader files:", files)

        # Get the last 4 bytes of the file
        bootloader_path = ""
        buff: bytes = b""
        print("Trying to find bootloader signature (AA55)")
        for file_ in files:
            with open(os.path.join(DRIVE_PATH, file_), "rb") as f:
                f.seek(-4, os.SEEK_END)
                buff = f.read(4)
                if buff == b"AA55":
                    bootloader_path = os.path.join(DRIVE_PATH, file_)
                if buff == b"A55\n":
                    f.seek(-5, os.SEEK_END)
                    buff = f.read(4)
                    if buff == b"AA55":
                        bootloader_path = os.path.join(DRIVE_PATH, file_)

        # Make bootinfo file
        if not bootloader_path:
            print("No bootloader found. Please install a bootloader.")
            return ""
        else:
            print("Writing boot.info ...")
            with open(bootinfo_path, "wb") as f:
                data = bootloader_path + "\n" + platform.system().lower()
                f.write(data.encode("utf-8"))
    else:
        with open(bootinfo_path, "rb") as f:
            bootloader_path = f.read().decode("utf-8").split("\n")
            required_os = bootloader_path[1]
            bootloader_path = bootloader_path[0]

        if not required_os == platform.system().lower():
            print("Boot.Info file was created in another OS!")
            os.remove(bootinfo_path)
            bootloader_path = search_for_bootloader()

        if not os.path.exists(bootloader_path):
            print("Boot.Info file doesn't contain a valid path, rewriting...")
            os.remove(bootinfo_path)
            bootinfo_path = search_for_bootloader()

    return bootloader_path

def run_bootloader(file_path: str, mem: memory.Memory, bios_ram_start_addr: int, fb: Framebuffer) -> tuple:
    set_mem(mem)

    size_of_bl: int = os.stat(file_path).st_size

    if size_of_bl > 512:
        return ("!ERROR!", None, None, None)

    with open(file_path, "rb") as f:
        f.seek(0)
        mem.write_ram(f.read(), bios_ram_start_addr)

    set_framebuffer(fb)

    exec_globals = {}
    exec_globals["__int__"] = interrupt

    print("Running Bootloader...")
    try:
        exec(mem.get_ram(size_of_bl, bios_ram_start_addr).decode("utf-8"), exec_globals)
    except Exception as e:
        return (str(e), SystemData, drive_data, DRIVE_PATH)

def start() -> str:
    GetSystemInfoBIOS()
    get_drive_data()
    file_ = search_for_bootloader()
    set_sys_data(SystemData)
    set_disk_data(disk_data)
    return file_
