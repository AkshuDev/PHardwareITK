import ctypes
import os
from ctypes import c_int, c_ulong, c_char_p, c_void_p, POINTER, c_long

libX11 = ctypes.cdll.LoadLibrary("libX11.so.6")

# Define opaque X11 types
Display = c_void_p
Window = c_ulong

libX11.XCreateSimpleWindow.argtypes = [
    ctypes.c_void_p,  # Display*
    ctypes.c_ulong,   # Window (parent)
    ctypes.c_int,     # x
    ctypes.c_int,     # y
    ctypes.c_uint,    # width
    ctypes.c_uint,    # height
    ctypes.c_uint,    # border width
    ctypes.c_ulong,   # border color
    ctypes.c_ulong    # background color
]
libX11.XCreateSimpleWindow.restype = ctypes.c_ulong
libX11.XDefaultScreen.argtypes = [Display]
libX11.XDefaultScreen.restype = c_int

libX11.XRootWindow.argtypes = [Display, c_int]
libX11.XRootWindow.restype = Window

libX11.XStoreName.argtypes = [Display, Window, c_char_p]
libX11.XStoreName.restype = c_int

libX11.XSelectInput.argtypes = [Display, Window, c_long]
libX11.XSelectInput.restype = c_int

libX11.XMapWindow.argtypes = [Display, Window]
libX11.XMapWindow.restype = c_int

libX11.XPending.argtypes = [Display]
libX11.XPending.restype = c_int

libX11.XGetWindowAttributes.argtypes = [Display, Window, c_void_p]
libX11.XGetWindowAttributes.restype = c_int

libX11.XDestroyWindow.argtypes = [Display, Window]
libX11.XDestroyWindow.restype = c_int

libX11.XFlush.argtypes = [Display]
libX11.XFlush.restype = c_int

_display = None

# Core X types
Atom     = ctypes.c_ulong
Window   = ctypes.c_ulong
Drawable = ctypes.c_ulong
Time     = ctypes.c_ulong
XPointer = ctypes.c_char_p
Bool     = ctypes.c_int
Colormap = ctypes.c_ulong
VisualID = ctypes.c_ulong

class XAnyEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("serial", ctypes.c_ulong),
        ("send_event", Bool),
        ("display", ctypes.c_void_p),
        ("window", Window),
    ]

class XKeyEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("serial", ctypes.c_ulong),
        ("send_event", Bool),
        ("display", ctypes.c_void_p),
        ("window", Window),
        ("root", Window),
        ("subwindow", Window),
        ("time", Time),
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("x_root", ctypes.c_int),
        ("y_root", ctypes.c_int),
        ("state", ctypes.c_uint),
        ("keycode", ctypes.c_uint),
        ("same_screen", Bool),
    ]

class XButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("serial", ctypes.c_ulong),
        ("send_event", Bool),
        ("display", ctypes.c_void_p),
        ("window", Window),
        ("root", Window),
        ("subwindow", Window),
        ("time", Time),
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("x_root", ctypes.c_int),
        ("y_root", ctypes.c_int),
        ("state", ctypes.c_uint),
        ("button", ctypes.c_uint),
        ("same_screen", Bool),
    ]

class XConfigureEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("serial", ctypes.c_ulong),
        ("send_event", Bool),
        ("display", ctypes.c_void_p),
        ("event", Window),
        ("window", Window),
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("width", ctypes.c_int),
        ("height", ctypes.c_int),
        ("border_width", ctypes.c_int),
        ("above", Window),
        ("override_redirect", Bool),
    ]

# Now build the XEvent union
class XEvent(ctypes.Union):
    _fields_ = [
        ("type", ctypes.c_int),
        ("xany", XAnyEvent),
        ("xkey", XKeyEvent),
        ("xbutton", XButtonEvent),
        ("xconfigure", XConfigureEvent),
        ("pad", ctypes.c_byte * 192),  # ensures correct size (192 bytes)
    ]
    
libX11.XNextEvent.argtypes = [Display, POINTER(XEvent)]
libX11.XNextEvent.restype = c_int

def _get_display():
    global _display
    if not _display:
        libX11.XOpenDisplay.restype = Display
        _display = libX11.XOpenDisplay(None)
        if not _display:
            raise RuntimeError("Unable to Open X11 Display")
    
    return _display

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
    display = _get_display()

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
    
    event_mask = (1 << 17) | (1 << 15) | (1 << 2) | (1 << 3)
    libX11.XSelectInput(display, window, event_mask)
    libX11.XMapWindow(display, window)

    return (display, window)

def show_window(window_tuple):
    display, window = window_tuple
    libX11.XMapWindow(display, window)
    libX11.XFlush(display)
    
def hide_window(window_tuple):
    display, window = window_tuple
    libX11.XUnmapWindow(display, window)
    libX11.XFlush(display)
    
def set_window_title(window_tuple, title):
    display, window = window_tuple
    libX11.XStoreName(display, window, title.encode("utf-8"))
    
def destroy_window(window_tuple):
    display, window = window_tuple
    libX11.XDestroyWindow(display, window)
    libX11.XFlush(display)

def poll_events(window_tuple):
    display, window = window_tuple
    event = XEvent()
    events = []

    while libX11.XPending(display):
        libX11.XNextEvent(display, ctypes.byref(event))
        events.append(event)
    return events

def is_window_alive(window_tuple) -> bool:
    display, window = window_tuple
    attrs = ctypes.c_ulong()
    status = libX11.XGetWindowAttributes(display, window, ctypes.byref(attrs))
    return status != 0