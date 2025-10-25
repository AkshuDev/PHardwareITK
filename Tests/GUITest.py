import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.GUI import gui
from phardwareitk.Extensions import *

def main(window, icon, renderer, winsurface) -> int:
    gui.AddIcon(window, icon)

    gui.SetBackgroundColor(window, Color("black", 0))

    gui.TitleBarWindows("Test", "dark")

    #rect = gui.Quadrilateral(100, 100).Draw(window)

    shape = gui.Shape(((100, 100), (200, 100), (100, 200), (200, 200)), wireframe=True).Draw(renderer)

    gui.UpdateWindow(window)

    gui.EventLoop(True, window, None, icon, renderer, False)

    return 0

def safeMain() -> int:
    gui.initialize()

    gui.PError = True

    window = gui.CreateWindow("Test")

    winsurface = gui.WindowSurface(window)

    renderer = gui.MakeRenderer(window)

    icon = PIcon("./Tests/HGame.png")

    errorCode = 0
    try:
        errorCode = main(window, icon, renderer, winsurface)
    except Exception as e:
        gui.SafeExitSDL(f"Safe Exit Activated, Error -> {e}", gui.DestroyWindow, (window, icon, renderer))

    return errorCode

if __name__ == "__main__":
    sys.exit(safeMain())