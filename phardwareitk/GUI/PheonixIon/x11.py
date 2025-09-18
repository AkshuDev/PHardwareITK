import ctypes
import os
from ctypes import c_int, c_ulong, c_char_p, c_void_p, POINTER

libX11 = ctypes.cdll.LoadLibrary("libX11.so.6")

# Define opaque X11 types
Display = c_void_p
Window = c_ulong
XEvent = ctypes.c_byte * 24  # Generic XEvent struct size (platform dependent!)

class PIX11Flags:
    def __init__(self, x=100, y=100, width=800, height=600, border=1, border_color=0, background=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.border_color = border_color
        self.background = background

def create_window(title: str="Pheonix Ion", width:int=800, height:int=600, flags:PIX11Flags=None):
    display = libX11.XOpenDisplay(None)
    if not display:
        raise RuntimeError("Cannot open X11 display")

    screen = libX11.XDefaultScreen(display)
    root = libX11.XRootWindow(display, screen)

    if not flags:
        flags = PIX11Flags(100, 100, width, height, 1, 0, 0)

    window = libX11.XCreateSimpleWindow(
        display,
        root,
        flags.x,
        flags.y,
        flags.width,
        flags.height,
        flags.border,
        flags.border_color,
        flags.background
    )

    libX11.XStoreName(display, window, title.encode("utf-8"))
    libX11.XSelectInput(display, window, 0x000001)  # ExposureMask
    libX11.XMapWindow(display, window)

    return (display, window)

def show_window(window_tuple):
    display, window = window_tuple
    libX11.XMapRaised(display, window)

def poll_events(window_tuple):
    display, window = window_tuple
    event = XEvent()
    events = []

    while libX11.XPending(display):
        libX11.XNextEvent(display, ctypes.byref(event))
        events.append({"type": "X11_EVENT", "raw": bytes(event)})
    return events
