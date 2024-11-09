import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk import HGame

print("HGAME - Details ->\n1. stdout, console\n2. stdin, window\n3. debug-stdout")

HGame.Initialize(True, "console", "window", 0)

window = HGame.Screen()
window.Loop()