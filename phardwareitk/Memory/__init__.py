"""Memory Allocation and such functions for python.
"""

import platform
import os
import sys

module_path:str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if not module_path in sys.path:
    sys.path.append(module_path)

os_:str = platform.system()
os_ = os_.lower()
win32:bool = False
posix:bool = False
unknown:bool = True

posix_os = [
    "linux", "unix", "euleros", "macos", "openbsd", "plan9", "vxworks", "minix",
    "ubuntu", "debian", "fedora", "arch", "aix", "hp-ux", "solaris",
    "netbsd", "freebsd", "dragonflybsd", "qnx", "illumos", "truenas",
    "redhat", "centos", "rocky linux", "almalinux", "suse", "gentoo",
    "slackware", "mandriva", "scientific linux", "oracle linux"
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

def force_os(_os:str, posix_based_os:bool=False) -> None:
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

if win32:
    #from phardwareitk.Memory._platform import _win32 as memory
    pass

if posix:
    #from phardwareitk.Memory._platform import _posix as memory
    pass

if unknown:
    #raise Exception("Cannot get OS try to force OS instead!")
    pass

if os_ != "" and (not unknown and (not win32 and not posix)):
    print("Sorry this is a unsupported or unimplemented OS, Exiting...")
    exit(1)
