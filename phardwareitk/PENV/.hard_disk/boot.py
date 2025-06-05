# Boots up AOS Kernel
# Table
__sys_info__ = __int__(0x9)
__drive_info__ = __int__(0x8)

table = {
	"filename": "AOS_Kernel.py",
	"args: __sys_info__, __drive_info__
}
__int__(0x51, table)
