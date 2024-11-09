import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.GUI import windows_gui

hwnd = windows_gui.CreateWindow("Test", "HI", x=100, y=100)
if hwnd:
    print(f"Window handle: {hwnd}")
    # Run the message loop
    windows_gui.MessageLoop(hwnd)
else:
    print("Window creation failed.")