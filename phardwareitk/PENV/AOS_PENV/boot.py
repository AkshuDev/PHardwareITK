# Boots up AOS Kernel
# Table
__sys_info__ = __int__(0x9)# type:ignore
__drive_info__ = __int__(0x8)# type:ignore

ptable = {
    "lba": 1,
    "size": 60,
}

__int__(0x51, ptable)
#AA55