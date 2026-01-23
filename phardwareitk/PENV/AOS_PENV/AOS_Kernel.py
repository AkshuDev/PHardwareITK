_cd_ = "home"  # Current directory
_cd_backup = "home"
_user = "admin"
_pass = None

print("Kernel Loaded in Protected Mode!", flush=True)

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
    print("", flush=True)

_p_sys_info()
