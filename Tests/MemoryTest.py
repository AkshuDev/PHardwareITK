import os
import sys
import platform
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.Memory import *

def Proc1(text):
    print(text)

def Proc2():
    hi = "HI from proc2!"
    Proc1(hi)

def Proc3():
    myint = 1
    myint = 2
    print(myint)

mem = memory.Memory(20, debug=True)
proc1_data = memory.Process_Data(0x0001, Proc1, "Hi from proc1!")
exec_data = memory.Execution_Data()
proc2_data = memory.Process_Data(0x0010, Proc2)
proc3_data = memory.Process_Data(0x0002, Proc3)

proc_man = memory.Process_Manager(mem)

proc_man.start_debug_server()

python_exe = sys.executable
client_script = os.path.join(os.path.dirname(__file__), "MemoryDebugTerm.py")

os_ = platform.system().lower()

if os_ == "windows":
    subprocess.Popen([
        "powershell", "-NoExit", "-Command",
        f"{python_exe} '{client_script}'"
    ])
elif os_ == "linux" or os == "macos":
    subprocess.Popen([
        "gnome-terminal", "--", python_exe, client_script
    ])
else:
    print("Unsupported OS so no debug Terminal for you!")

proc_man.add_proc(exec_data, proc1_data)
proc_man.add_proc(exec_data, proc2_data)
proc_man.add_proc(exec_data, proc3_data)
proc_man.run_next()
proc_man.run_next()
proc_man.run_next()
proc_man.stop_proc(0x0001)
proc_man.stop_proc(0x0010)
proc_man.stop_proc(0x0002)