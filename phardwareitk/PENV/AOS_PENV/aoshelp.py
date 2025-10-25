from typing import *

def cmd_aos_help(print_:bool, flush:bool=False, endl:str="\n") -> Optional[None, str]:
	"""AOS cmd help func"""
	help_ = """Usage: aos <command> <params>
	
aos is a command by AOS which allows users to run commands that interact with the system directtly which is not possible normally.
	
Basic Commands:
	wipe-drive: aos wipe-drive
		Wipes and then partions drive in PBFS (Python Based File System/Pheonix Base File System)
		If you use this command all data will be lost excluding the OS itself.
	
	cd-usr: aos cd-usr <user>
		Changes the default user (admin) to another valid user
		
	mk-usr: aos mk-usr <username> <options>
		Makes a new user with the specified username.
		
		OPTIONS:
			-p: defines a password for the user created
	
	rm-usr: aos rm-usr <user>
		Removes the specified user from the system
		
	rn-usr: aos rn-usr <user> <username>
		Renames a user with the specified username
		
Display Commands:
	display-mode: aos display-mode <mode as a number>
		Changes the default display mode.
		
		Modes:
			0 -> Command Line Interface
			1 -> VGA
			2 -> FrameBuffer
			3 -> PHardwareITK.GUI (Not recommended as it is a sdl2 package and may be slower to run)
			
		Default Modes:
			AOS:Penv:Potato -> Command Line Interface
			AOS:Penv:Full -> VGA (at booting), Framebuffer (For the rest of the time)
"""

	if not print_:
		return help_
		
	print(help_, flush, end=endl)
