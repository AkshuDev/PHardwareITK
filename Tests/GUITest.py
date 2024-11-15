import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.GUI import gui
from phardwareitk.Extensions import *

def main() -> int:
    gui.initialize()

    window = gui.CreateWindow("Test")

    winsurface = gui.WindowSurface(window)

    icon = PIcon("./Tests/sample1.bmp")

    gui.AddIcon(window, icon)

    gui.SetBackgroundColor(window, Color("black", 0))

    button = gui.Button(50, 50, 200, 50)
    renderer = button.Draw(window)
    WidgetButton = button.onClick(print, ("Hello World!", "AMAZING!"))

    if isinstance(renderer, bytes):
        gui.SafeExitSDL(renderer.decode(), gui.DestroyWindow, (window, icon))
        return 1

    gui.UpdateWindow(window)

    gui.EventLoop(True, window, [WidgetButton], icon, renderer)

    return 0

if __name__ == "__main__":
    sys.exit(main())