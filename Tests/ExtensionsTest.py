import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.Extensions import *
from phardwareitk.Extensions.HyperOut import *
from phardwareitk.Extensions.HyperIn import *

printH("Hello,", "This is a test!", FontEnabled=True, Font=TextFont(font_color=Color("blue")))

msgOld = input("This is a normal input!: ")
print("You wrote:", msgOld)

msg2 = inputH("This is Hyper Input: ", FontEnabled=True, Font=TextFont(font_color=Color("cyan")))
print("You wrote:", msg2)

msg = inputH("This is Hyper Input with Mask enabled: ", FontEnabled=True, Font=TextFont(font_color=Color("cyan")), mask=True)
print("You wrote:", msg)

msg = inputH("This is Hyper Input with History Enabled: ", FontEnabled=True, Font=TextFont(font_color=Color("cyan")), History=[msg, msg2, msgOld])
print("You wrote:", msg)

import time

run = True

progressH(False, (0, "cpos-3"), 0, 5)

for i in range(5):
    progressH(False, (0, "cpos-3"), i + 1, 5, onMaxMsg="  : MAX reached!", First=False)

    time.sleep(1)

print("Making a cache file for print function...")
result = cacheH(".\\testCache.cache", print, None)

print("Done!")

print("Loading from cache...")
result = cacheH(".\\testCache.cache")
print("Result:", result)
exitH(0, "Just a Normal Exit")