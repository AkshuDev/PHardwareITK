import os
import platform
import json

mem = None
vga = None
framebuffer = None
disk_data = None
sys_data = None

posix_os = [
    "linux",
    "unix",
    "euleros",
    "macos",
    "openbsd",
    "plan9",
    "vxworks",
    "minix",
    "ubuntu",
    "debian",
    "fedora",
    "arch",
    "aix",
    "hp-ux",
    "solaris",
    "netbsd",
    "freebsd",
    "dragonflybsd",
    "qnx",
    "illumos",
    "truenas",
    "redhat",
    "centos",
    "rocky linux",
    "almalinux",
    "suse",
    "gentoo",
    "slackware",
    "mandriva",
    "scientific linux",
    "oracle linux",
]

class PenvInturruptReturn(Exception):
    def __init__(self, *values):
        self.values = values
        super().__init__(*values)

    def __str__(self):
        val = ""
        for value in self.values:
            val += str(value) + " "
        return val

    def __repr__(self):
        return self.__str__()

def set_mem(memory: object) -> None:
    global mem
    if memory == None:
        return
    mem = memory

def set_vga(vga_: object) -> None:
    global vga
    if vga_ == None:
        return
    vga = vga_

def set_framebuffer(framebuffer_: object) -> None:
    global framebuffer
    if framebuffer_ == None:
        return
    framebuffer = framebuffer_

def set_disk_data(disk_data_: object) -> None:
    global disk_data
    if disk_data_ == None:
        return
    disk_data = disk_data_

def set_sys_data(sys_data_: object) -> None:
    global sys_data
    if sys_data_ == None:
        return
    sys_data = sys_data_

def interrupt(code: int, *args):
    global mem
    global vga
    global framebuffer
    global sys_data
    global disk_data

    if code == 0x0:  # Write
        print(*args)
    elif code == 0x1:  # Read
        return input(args[0])
    elif code == 0x2:  # Clear
        if platform.system().lower() == "windows":
            os.system("cls")
        elif platform.system().lower() in posix_os:
            os.system("cls")
        else:
            print("\033[2J\033[H")

    elif code == 0x51:  # Shift to PMode
        table: dict = args[0]
        table["type"] = 0x51
        return_ = json.dumps(table)
        raise PenvInturruptReturn(return_)  # Stop the exec function
    elif code == 0x60:  # Call file and exit
        table: dict = {"type": 0x60, "filename": args[0]}
        return_ = json.dumps(table)
        raise PenvInturruptReturn(return_)

    elif code == 0x4:  # Get Ram
        if not mem:
            return None
        else:
            return mem.get_ram(args[0], args[1])
    elif code == 0x5:  # Get VGA
        if not vga:
            return None
        else:
            return vga.serialize()
    elif code == 0x6:  # Frambuffer Write
        if not framebuffer:
            return None
        else:
            return framebuffer.write_pixel(args[0], args[1], args[2], args[3], args[4])
    elif code == 0x7:  # VGA Write
        if not vga:
            return None
        else:
            return vga.write_pixel(args[0], args[1], args[2], args[3], args[4])
    elif code == 0x8:  # Get Disk Data
        return disk_data
    elif code == 0x9:  # Get Sys Data
        return sys_data
    elif code == 0x10:  # Write mem func
        if not mem:
            return None
        else:
            return mem.write_ram(args[0], args[1], args[2])
    elif code == 0x11:  # Get Ram
        if not mem:
            return None
        else:
            ram = mem.ram
            mem.ram = None
            return ram
    elif code == 0x12:  # Return RAM
        mem.ram = args[0]
    elif code == 0x13:  # Framebuffer Clear
        if not framebuffer:
            return None
        else:
            return framebuffer.clear()
    elif code == 0x14:  # Framebuffer Render
        if not framebuffer:
            return None
        else:
            return framebuffer.render()

def ddh_key(dict_: dict, key: str) -> bool:
    try:
        val = dict_[key]
        return True
    except Exception:
        return False

def get_os() -> tuple[bool, bool, bool, str]:
	os_ = platform.system().lower()
	win32: bool = False
	posix: bool = False
	unknown: bool = True

	posix_os = [
		"linux",
		"unix",
		"euleros",
		"macos",
		"openbsd",
		"plan9",
		"vxworks",
		"minix",
		"ubuntu",
		"debian",
		"fedora",
		"arch",
		"aix",
		"hp-ux",
		"solaris",
		"netbsd",
		"freebsd",
		"dragonflybsd",
		"qnx",
		"illumos",
		"truenas",
		"redhat",
		"centos",
		"rocky linux",
		"almalinux",
		"suse",
		"gentoo",
		"slackware",
		"mandriva",
		"scientific linux",
		"oracle linux",
	]

	if os_ == "windows":
		win32 = True
		unknown = False
		posix = False
	elif os_ in posix_os:
		posix = True
		unknown = False
		win32 = False
	else:
		unknown = True
		win32 = False
		posix = False

	return (win32, posix, unknown, os_)