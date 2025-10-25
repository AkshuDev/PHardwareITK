import os
import sys

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if not PATH in sys.path:
    sys.path.insert(0, PATH)

from phardwareitk.GUI.pheonix_ion import *

print("Creating Ion...")
ionhandler = PheonixIon()
print("Creating Window...")
win = ionhandler.create_window()
# print("Attaching GPU Context")
# ctx = ionhandler.get_gpu(win)
# ionhandler.attach_gpu(win, ctx)
print("Handle: ", ionhandler.get_native_handle(win))
print("Handles: ", ionhandler.windows)
running = True
ionhandler.show_window(win)

print("Polling...")
r = 0
g = 0
b = 0
a = 255
while running:
    event: list[PIonEvent] = ionhandler.poll_events(win)
    if len(event) == 0: continue
    if event[0].type == PIonEvent_Types.LEFT_DOWN:
        ctx.driver.clear(r, g, b, a)
        r += 10
        g += 5
        b += 2
    elif event[0].type == PIonEvent_Types.DESTROY:
        ionhandler.destroy_window(win)
        running = False

print("Destroying Window...")
ionhandler.destroy_window(0)
print("Done!")