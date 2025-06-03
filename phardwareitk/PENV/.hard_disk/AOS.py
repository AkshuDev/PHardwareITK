def print(*args):
	__int__(0x0, *args) # type: ignore

__sys_info__ = __int__(0x9) # type: ignore
__drive_info__ = __int__(0x8) # type: ignore

# Shift To Protected Mode
table:dict = {
	"filename": "AOS_Kernel.py",
	"args": [__drive_info__, __sys_info__]
}

__int__(0x51, table) # type: ignore
