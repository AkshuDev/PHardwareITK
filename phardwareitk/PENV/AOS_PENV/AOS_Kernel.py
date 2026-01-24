_kernel_start = ""

def _p_sys_info() -> None:
    print("CPU cores:", int_to_str(__system_info__["cpu_cores"]))
    print("CPU Arch:", __system_info__["cpu_architecture"])
    print("CPU Name:", __system_info__["processor_name"])
    print("Host Name:", __system_info__["host_name"])
    print("Host System:", __system_info__["host_system"])
    print("Host Version:", __system_info__["host_version"])
    print("Host Release:", __system_info__["host_release"])
    print("Host Platform:", __system_info__["host_platform"])
    print("Host Uname:", __system_info__["host_uname"])
    print("Host Ram Size (Bytes):", int_to_str(__system_info__["ram_size"]))
    print("Host Ram Size (MB):", float_to_str(__system_info__["ram_size"] / 1024**2))
    print("Host Ram Size (GB):", float_to_str(__system_info__["ram_size"] / 1024**3))
    print("Host Storage Size (Bytes):", int_to_str(__system_info__["storage_size"]))
    print("Host Storage Size (MB):", float_to_str(__system_info__["storage_size"] / 1024**2))
    print("Host Storage Size (GB):", float_to_str(__system_info__["ram_size"] / 1024**3))
    print("", flush=True, endl=False)

def aos_shell_help():
    print("Commands:")
    print("\tsysinfo: Prints system information")
    print("\tshutdown: Shutdown AOS")
    print("\tclear: Clears the screen")
    print("\thelp: Prints this help message")
    print("", endl=False, flush=True)

_cmd = ""
_running = True
_cd_ = "home"  # Current directory
_cd_backup = "home"
_user = "admin"
if not kbd_enable_scanning():
    _running = False
    print("Could not enable PS2 Keyboard Scanning! Shutting Down!", flush=True)
    
while _running:
    _cmd = input(_cd_ + " $: ")
    if _cmd == "sysinfo":
        _p_sys_info()
        continue
    elif _cmd == "shutdown":
        _running = False
        continue
    elif _cmd == "clear":
        clear()
        continue
    elif _cmd == "help":
        aos_shell_help()
    else:
        print("Unknown command:", _cmd, "\n\tMaybe try using help?", flush=True)