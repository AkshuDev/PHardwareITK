import os
import sys

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if not PATH in sys.path:
    sys.path.insert(0, PATH)

from phardwareitk.GUI.pheonix_ion import *

print("Creating Ion...")
ionhandler = PheonixIon()
print("Creating Window...")
ionhandler.create_window()
running = True
i = 0

print("Polling...")
while running:
    event = ionhandler.poll_events(0)
    if i == 10000000 :
        running = False
    i += 1

print("Destroying Window...")
ionhandler.destroy_window(0)
print("Done!")