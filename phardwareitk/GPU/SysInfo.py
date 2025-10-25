import platform
import os

platform = platform.system().lower()

Windows = True if platform == "windows" else False
Linux = True if platform == "linux" else False
Kali = True if platform == "kali" else False
MacOs = True if platform == "darwin" else False
Ubuntu = True if platform == "ubuntu" else False