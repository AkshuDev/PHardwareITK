# Boots up AOS Kernel
# Table
__sys_info__ = __int__(0x9)# type:ignore
__drive_info__ = __int__(0x8)# type:ignore

table = {
	"filename": "AOS_Kernel.py",
	"args": [__sys_info__, __drive_info__]
}
__int__(0x51, table) #type:ignore
#AA55