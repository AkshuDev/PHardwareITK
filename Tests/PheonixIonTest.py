import os
import sys

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if not PATH in sys.path:
    sys.path.insert(0, PATH)

from phardwareitk.GUI.pheonix_ion import *

print("Creating Ion...")
ionhandler = PheonixIon()
print("Creating Window...")
win = ionhandler.create_window("Ion", 800, 600)
# print("Attaching GPU Context")
# ctx = ionhandler.get_gpu(win)
ctx = None

print("Handle: ", ionhandler.get_native_handle(win))
print("Handles: ", ionhandler.windows)
running = True
ionhandler.show_window(win)

# ionhandler.attach_gpu(win, ctx)
# ctx.driver.viewport(800, 600)

print("Polling...")
r = 0
g = 0
b = 0
a = 255
while running:
    event: list[PIonEvent] = ionhandler.poll_events(win)
    if len(event) == 0: continue
    for e in event:
        if e.type == PIonEvent_Types["LEFT_DOWN"]:
            ctx.driver.clear(r, g, b, a)
            ctx.driver.swap()
            if r < 245:
                r += 10
            if g < 250:
                g += 5
            if b < 253:
                b += 2
        elif e.type == PIonEvent_Types["DESTROY"]:
            ctx.driver.destroy_context()
            ionhandler.destroy_window(win)
        elif e.type == PIonEvent_Types["CLOSE"]:
            ctx.driver.destroy_context()
            ionhandler.destroy_window(win)
        elif e.type == PIonEvent_Types["QUIT"]:
            running = False

print("Done!")