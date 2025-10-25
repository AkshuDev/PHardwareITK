import os
import sys
import time
import json
import platform
import threading
import gc

os_files: list = [__file__]

path = sys.argv[1]
if not path in sys.path:
    sys.path.append(path)

from Memory import *

_mem = Memory(int(sys.argv[2]), int(sys.argv[3]))  # type: ignore
_mem.sys_block = MemBlock(64, os_files, "AOS-BLOCK-KERNEL", 0)  # type: ignore

_penv_path = sys.argv[5]
_drive_info = sys.argv[6]
_sys_info = json.loads(sys.argv[7])

if not _penv_path in sys.path:
    sys.path.append(_penv_path)

from PBFS import PBFS_DriveData

from AOS_FHD import setup_dir_tree

_file_manager = PBFS_DriveData()
_cd_ = "home"  # Current directory
_cd_backup = "home"
_user = "admin"
_pass = None

_file_manager.reload() # Reload the file manager

_cd_, _user = setup_dir_tree(_file_manager, _cd_, _user)

_file_manager.reload()

print("Kernel Loaded in Protected Mode!")

base_mode = "cli"

x: int = 0
y: int = 0

cmd = ""

def _p_sys_info() -> None:
    print("CPU cores:", str(_sys_info["cpu_cores"]))
    print("CPU Arch:", str(_sys_info["cpu_architecture"]))
    print("CPU Name:", str(_sys_info["processor_name"]))
    print("Host Name:", str(_sys_info["host_name"]))
    print("Host System:", str(_sys_info["host_system"]))
    print("Host Version:", str(_sys_info["host_version"]))
    print("Host Release:", str(_sys_info["host_release"]))
    print("Host Platform:", str(_sys_info["host_platform"]))
    print("Host Uname:", str(_sys_info["host_uname"]))
    print("Host Ram Size (GB):", str(_sys_info["ram_size"]))
    print("Host Storage Size (GB):", str(_sys_info["storage_size"]))

if _pass is not None:
    in_ = input("Password for User", _user, ": ")
    while True:
        if not in_ == _pass:
            print("Sorry wrong password, try again or type either shutdown or poweroff")
        else:
            print("Welcome!")
            break

        in_ = input("Password: ")

while True:
    cmd = input(f"{_cd_}\n|\n ---$: ").lower()
    cmd = cmd.split(" ")

    if cmd[0] == "poweroff" or cmd[0] == "shutdown":
        print("Shutting down the system...")
        break

    elif cmd[0] == "clear" or cmd[0] == "cls":
        os.system('cls' if platform.system().lower() == 'windows' else 'clear')

    elif cmd[0] == "wipe-current-user":
        sure = input("Are you sure you want to wipe the current user? (yes/no): ").lower()
        if sure == "yes":
            debug = False
            if len(cmd) > 1:
                if "-d:t" == cmd[1]:
                    debug = True

            _file_manager.reload()  # Reload the file manager to ensure we have the latest state
            print(f"Wiping current user data [{_file_manager.join_path(b'home', b'usrs', _user.encode('utf-8')).decode('utf-8')}]...")
            out = _file_manager.rm_dir(_file_manager.join_path(b"home", b"usrs", _user.encode("utf-8")), debug)
            if out != 0:
                print("Error wiping default user data:", out)
                continue
            print("Current user data wiped successfully!")
            print("Shutting Down...")
            break

    elif cmd[0] == "aos":
        # Get Param 1 as the command
        if not len(cmd) > 1:
            print("Usage: aos <command> <params>, use --help incase you don't know commands")
            continue

        cmd_aos = cmd[1]

        if cmd_aos == "--help":
            from aoshelp import cmd_aos_help
            cmd_aos_help(True, True)
            continue

        if cmd_aos == "wipe-drive":
            input_ = input("Are you sure, you want to erase everything? (Y/N): ")
            input_ = input_.lower()

            if not input_ == "y":
                continue

            from PBFS import start, PBFS_DriveData, PBFS_SuperBlock, init_vdrive
            init_vdrive(True)
            print("Drive is wiped, shutting down...")
            break

        elif cmd_aos == "cd-usr":
            if not len(cmd) > 2:
                print("Usage: aos cd-usr <user>")
                continue

            usr = cmd[2]

            user = _file_manager.join_path(b"home", b"usrs", usr.encode("utf-8")).decode("utf-8")

            if not _file_manager.dir_exists(user.encode("utf-8")):
                print("No such user exists!")

            out = _file_manager.write_file(b"home\\aosduser.aos", json.dumps({"user": f"home\\usrs\\{usr}_conf.aos"}).encode("utf-8"), [0x0, 0x5, (os_files, None)])
            if not out == 0:
                print("aos: ERROR, PBFS -", out)
                continue

        elif cmd_aos == "mk-usr":
            if not len(cmd) > 2:
                print("Usage: aos mk-usr <username> <OPTIONS>")
                continue

            usr = cmd[3]
            password = None

            if len(cmd) > 3:
                for option in cmd:
                    op = option.split(":")
                    if op[0] == "-p":
                        password = op[1]

            if password is None:
                password = 0xFFFF

            if "/\\=+{}'\";:,<>?!@#$%^&*()" in usr:
                print("Only alphabets, numbers and [-, _, .] are allowed in usernames")
                continue

            out = _file_manager.write_file(_file_manager.join_path(b"home", b"usrs", usr.encode("utf-8") + b"_conf.aos"), json.dumps({"name": usr, "password": password}).encode("utf-16"), [0x0, 0x5, os_files])

            if not out == 0:
                print("aos: ERROR, PBFS -", out)
                continue

        elif cmd_aos == "rm-usr":
            if not len(cmd) > 2:
                print("Usage aos rm-usr <user>")
                continue

            usr = cmd[3]
            user = _file_manager.join_path(b"home", b"usrs", usr.encode("utf-8"))

            if not _file_manager.dir_exists(user):
                print("No such user!")
                continue

            out = _file_manager.remove_file(user + b"_config.aos")

            if not out == 0:
                print("aos: ERROR, PBFS -", out)
                continue

            cmd = input("Verbose? (y/n): ").lower()

            if not cmd == "y":
                cmd = False
            else:
                cmd = True

            out = _file_manager.rm_dir(user, cmd)

            if not out == 0:
                print("aos: ERROR, PBFS -", out)
                continue

    elif cmd[0] == "sysinfo":
        print("System Information:")
        _p_sys_info()
    elif cmd[0] == "lsd":
        dir_ = None
        if len(cmd) > 1:
            dir_ = cmd[1]
        else:
            dir_ = input("Directory to list files in (leave empty for cd): ")
            if dir_ == "":
                dir_ = None

        if dir_ is None or dir_ == "":
            dir_ = _cd_

        if dir_.startswith("/") or dir_.startswith("\\"):
            dir_ = _file_manager.join_path(_cd_.encode("utf-8"), dir_.encode("utf-8")).decode("utf-8")

        print(f"Files/SubDirs in the directory [{dir_ if dir_ is not None else _cd_}]:")
        print(*_file_manager.list_dir(dir_), sep="\n")
    elif cmd[0] == "chf":
        src = None
        dst = None
        if len(cmd) > 2:
            src = cmd[1]
            dst = cmd[2]
        elif len(cmd) == 2:
            src = cmd[1]
            dst = input("Destination path in the file system: ")
        else:
            src = input("Source path on host system: ")
            dst = input("Destination path in the file system: ")

        data:bytes = b""

        if not os.path.exists(src):
            print("Source path does not exist!")
            continue
        else:
            with open(src, "rb") as f:
                data = f.read()

        dst = _file_manager.join_path(_cd_.encode("utf-8"), dst.encode("utf-8")).decode("utf-8")

        print("Copying file from host system to file system...")

        if isinstance(str, data):
            data.encode("utf-8")

        out = _file_manager.write_file(dst, data)
        if out != 0:
            print("Error copying file:", out)
        else:
            print("File copied successfully!")
    elif cmd[0] == "mvf":
        src = None
        dst = None
        if len(cmd) > 2:
            src = cmd[1]
            dst = cmd[2]
        elif len(cmd) == 2:
            src = cmd[1]
            dst = input("Destination path: ")
        else:
            src = input("Source path: ")
            dst = input("Destination path: ")

        src = _file_manager.join_path(_cd_.encode("utf-8"), src.encode("utf-8")).decode("utf-8")
        dst = _file_manager.join_path(_cd_.encode("utf-8"), dst.encode("utf-8")).decode("utf-8")

        print("Moving file from", src, "to", dst + "...")

        file_data = _file_manager.get_file(src)
        out = _file_manager.remove_file(src)
        if out != 0:
            print("Error removing file:", out)
        else:
            out = _file_manager.write_file(dst, file_data)
            if out != 0:
                print("Error writing file:", out)
            else:
                print("File moved successfully!")
    elif cmd[0] == "rmf":
        path = None
        if len(cmd) > 1:
            path = cmd[1]
        else:
            path = input("Path to remove: ")

        path = _file_manager.join_path(_cd_.encode("utf-8"), path.encode("utf-8")).decode("utf-8")

        print("Removing file at", path + "...")
        out = _file_manager.remove_file(path)
        if out != 0:
            print("Error removing file:", out)
        else:
            print("File removed successfully!")
    elif cmd[0] == "mkf":
        path:str = None
        data:str = None

        if len(cmd) > 2:
            path = cmd[1]
            data = _file_manager.get_file(cmd[2])
            if data == None:
                print("Error getting file data from path:", cmd[2])
                continue
        elif len(cmd) == 2:
            path = cmd[1]
        else:
            path = input("Path to create file: ")
            data = input("Data to write to the file (leave empty for no data): ")

        path = _file_manager.join_path(_cd_.encode("utf-8"), path.encode("utf-8")).decode("utf-8")

        print("Creating file at", path + "...")
        out = _file_manager.write_file(path.encode("utf-8"), data.encode("utf-8") if data else b"")
        if out != 0:
            print("Error creating file:", out)
        else:
            print("File created successfully!")
    elif cmd[0] == "gfc":
        path = ""
        if len(cmd) > 1:
            path = cmd[1]
        else:
            path = input("Path to get file from: ")

        path = _file_manager.join_path(_cd_.encode("utf-8"), path.encode("utf-8")).decode("utf-8")

        print("Getting file at", path + "...")
        file_data = _file_manager.get_file(path.encode("utf-8"))

        if not file_data:
            print("Error Getting file:", path)
            continue

        if isinstance(file_data, str):
            print("Error getting file:", file_data)
        else:
            print("File data:", file_data.decode("utf-8"))
    elif cmd[0] == "mkd":
        path = None
        if len(cmd) > 1:
            path = cmd[1]
        else:
            path = input("Path to create directory: ")

        path = _file_manager.join_path(_cd_.encode("utf-8"), path.encode("utf-8")).decode("utf-8")

        print("Creating directory at", path + "...")
        out = _file_manager.mk_dir(path.encode("utf-8"))
        if out != 0:
            print("Error creating directory:", out)
        else:
            print("Directory created successfully!")
    elif cmd[0] == "mvd":
        src = None
        dst = None
        if len(cmd) > 2:
            src = cmd[1]
            dst = cmd[2]
        elif len(cmd) == 2:
            src = cmd[1]
            dst = input("Destination path: ")
        else:
            src = input("Source path: ")
            dst = input("Destination path (the dir might be renamed, please include dir name at the end of the path): ")

        src = _file_manager.join_path(_cd_.encode("utf-8"), src.encode("utf-8")).decode("utf-8")
        dst = _file_manager.join_path(_cd_.encode("utf-8"), dst.encode("utf-8")).decode("utf-8")

        print("Moving directory from", src, "to", dst + "...")

        out = _file_manager.mv_dir(src.encode("utf-8"), dst.encode("utf-8"))
        if out != 0:
            print("Error moving directory:", out)
        else:
            print("Directory moved successfully!")
    elif cmd[0] == "rmd":
        path = None
        debug:bool = False

        if len(cmd) > 1:
            if "-d" in cmd[1]:
                debug = True if cmd[1] == "-d:t" else False
            else:
                path = cmd[1]
        elif len(cmd) > 2:
            path = cmd[1]
            debug = True if cmd[2] == "-d:t" else False
        else:
            path = input("Path to remove directory: ")

        path = _file_manager.join_path(_cd_.encode("utf-8"), path.encode("utf-8")).decode("utf-8")

        print("Removing directory at", path + "...")
        out = _file_manager.rm_dir(path.encode("utf-8"), debug)
        if out != 0:
            print("Error removing directory:", out)
        else:
            print("Directory removed successfully!")
    elif cmd[0] == "cd":
        if len(cmd) > 1:
            new_dir = cmd[1]
        else:
            new_dir = input("Enter directory to change to: ")

        if new_dir == "..":
                new_dir = new_dir.replace("..", "")
                if _cd_ != "home":
                    _cd_ = _cd_backup
                    if not _cd_backup == "home":
                        _cd_backup = _cd_backup.split("\\")
                        _cd_backup = _cd_backup[len(_cd_backup) - 2]
                    print("Changed directory to:", _cd_)
                else:
                    print("You are already in the home directory, cannot go up further.")
                    continue
        elif new_dir.startswith("./") or new_dir.startswith(".\\"):
            new_dir = new_dir.strip("./\\")
            new_dir = _file_manager.join_path(_cd_.encode("utf-8"), new_dir.encode("utf-8")).decode("utf-8")
            new_dir = new_dir.strip("./\\")
            new_dir_l = new_dir.replace("/", "\\").split("\\")
            cd_t = _cd_
            cd_backupt = _cd_backup
            work = True

            for part in new_dir_l:
                if part == "..":
                    cd_t = cd_backupt
                    if not cd_backupt == "home":
                        cd_backupL = cd_backupt.split("\\")
                        cd_backupL.pop(len(cd_backupL) - 1)
                        cd_backupt = "".join(*cd_backupL)
                else:
                    _cd_backup_t = _cd_
                    _cd_t = _file_manager.join_path(cd_t.encode("utf-8"), part.encode("utf-8")).decode("utf-8")
                    out = _file_manager.dir_exists(_cd_t.encode("utf-8"))
                    if out == False:
                        print("Directory doesn't exist:", _cd_t.encode("utf-8"))
                        work = False
                    else:
                        cd_t = _cd_t
                        cd_backupt = _cd_backup_t

            if work:
                _cd_ = cd_t
                _cd_backup = cd_backupt
                continue
        elif new_dir.startswith("~/") or new_dir.startswith("~\\"):
            new_dir = new_dir.strip("~/\\")
            new_dir = _file_manager.join_path(_cd_.encode("utf-8"), new_dir.encode("utf-8")).decode("utf-8")
            new_dir = new_dir.strip("~/\\")
            new_dir_l = new_dir.replace("/", "\\").split("\\")
            cd_t = "home"
            cd_backupt = "home"
            work = True

            for part in new_dir_l:
                if part == "..":
                    cd_t = cd_backupt
                    if not cd_backupt == "home":
                        cd_backupL = cd_backupt.split("\\")
                        cd_backupL.pop(len(cd_backupL) - 1)
                        cd_backupt = "".join(*cd_backupL)
                else:
                    _cd_backup_t = _cd_
                    _cd_t = _file_manager.join_path(cd_t.encode("utf-8"), part.encode("utf-8")).decode("utf-8")
                    out = _file_manager.dir_exists(_cd_t.encode("utf-8"))
                    if out == False:
                        print("Directory doesn't exist:", _cd_t.encode("utf-8"))
                        work = False
                    else:
                        cd_t = _cd_t
                        cd_backupt = _cd_backup_t

            if work:
                _cd_ = cd_t
                _cd_backup = cd_backupt
                continue
        else:
            new_dir = new_dir.strip("./\\")
            new_dir = _file_manager.join_path(_cd_.encode("utf-8"), new_dir.encode("utf-8")).decode("utf-8")
            new_dir = new_dir.strip("./\\")
            new_dir_l = new_dir.replace("/", "\\").split("\\")
            cd_t = _cd_
            cd_backupt = _cd_backup
            work = True

            for part in new_dir_l:
                if part == "..":
                    cd_t = cd_backupt
                    if not cd_backupt == "home":
                        cd_backupL = cd_backupt.split("\\")
                        cd_backupL.pop(len(cd_backupL) - 1)
                        cd_backupt = "".join(*cd_backupL)
                else:
                    _cd_backup_t = _cd_
                    _cd_t = _file_manager.join_path(cd_t.encode("utf-8"), part.encode("utf-8")).decode("utf-8")
                    out = _file_manager.dir_exists(_cd_t.encode("utf-8"))
                    if out == False:
                        print("Directory doesn't exist:", _cd_t.encode("utf-8"))
                        work = False
                    else:
                        cd_t = _cd_t
                        cd_backupt = _cd_backup_t

            if work:
                _cd_ = cd_t
                _cd_backup = cd_backupt
                continue

    elif cmd[0] == "tree-fs":
        print("Directory Tree (A-Z):")
        print("\nFiles:")
        print(*sorted(_file_manager.files), sep="\n")
        print("\nDirectories:")
        print(*sorted(_file_manager.dirs), sep="\n")
    elif cmd[0] == "reload-fs":
        print("Reloading file manager...")
        _file_manager.reload()
        print("File manager reloaded successfully!")

    else:
        print("Unknown command:", cmd[0])
