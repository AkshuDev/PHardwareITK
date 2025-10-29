# X11 YOU MADE MY LIFE A LIVING NIGHTMARE!!!!!!
# TOTAL HOURS WASTED: 9

import ctypes
import os
from ctypes import c_int, c_ulong, c_char_p, c_void_p, POINTER, c_long, c_uint, cdll

from phardwareitk.GPU._base import BaseGPUD
from phardwareitk.GUI.PheonixIon.types import *
from phardwareitk.GUI.pheonix_ion import GPU_API, PIonContext

libX11 = ctypes.cdll.LoadLibrary("libX11.so.6")

# Define opaque X11 types
Display = c_void_p
Window = c_ulong

# Core X types
# Not organised looks better as a dev, truely saying!
Atom = ctypes.c_ulong
Window = ctypes.c_ulong
Drawable = ctypes.c_ulong
Time = ctypes.c_ulong
XPointer = ctypes.c_char_p
Bool = ctypes.c_int
Colormap = ctypes.c_ulong
VisualID = ctypes.c_ulong

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

class XSetWindowAttributes(ctypes.Structure):
    _fields_ = [
        ("background_pixmap", c_ulong),
        ("background_pixel", c_ulong),
        ("border_pixmap", c_ulong),
        ("border_pixel", c_ulong),
        ("bit_gravity", c_int),
        ("win_gravity", c_int),
        ("backing_store", c_int),
        ("backing_planes", c_ulong),
        ("backing_pixel", c_ulong),
        ("save_under", Bool),
        ("event_mask", c_long),
        ("do_not_propagate_mask", c_long),
        ("override_redirect", Bool),
        ("colormap", Colormap),
        ("cursor", c_ulong),
    ]

class XWindowAttributes(ctypes.Structure):
    _fields_ = [
        ("x", c_int),
        ("y", c_int),
        ("width", c_int),
        ("height", c_int),
        ("border_width", c_int),
        ("depth", c_int),
        ("visual", c_void_p),
        ("root", Window),
        ("class_", c_int),
        ("bit_gravity", c_int),
        ("win_gravity", c_int),
        ("backing_store", c_int),
        ("backing_planes", c_ulong),
        ("backing_pixel", c_ulong),
        ("save_under", Bool),
        ("colormap", Colormap),
        ("map_installed", Bool),
        ("map_state", c_int),
        ("all_event_masks", c_long),
        ("your_event_mask", c_long),
        ("do_not_propagate_mask", c_long),
        ("override_redirect", Bool),
        ("screen", c_void_p),
    ]

class XVisualInfo(ctypes.Structure):
    _fields_ = [
        ("visual", ctypes.c_void_p),
        ("visualid", ctypes.c_ulong),
        ("screen", ctypes.c_int),
        ("depth", ctypes.c_int),
        ("class_", ctypes.c_int),
        ("red_mask", ctypes.c_ulong),
        ("green_mask", ctypes.c_ulong),
        ("blue_mask", ctypes.c_ulong),
        ("colormap_size", ctypes.c_int),
        ("bits_per_rgb", ctypes.c_int),
    ]

libX11.XCreateSimpleWindow.restype = ctypes.c_ulong
libX11.XCreateWindow.argtypes = [
    Display, Window,
    c_int, c_int, c_uint, c_uint, c_uint,
    c_int, c_uint, c_void_p,
    c_ulong, POINTER(XSetWindowAttributes)
]
libX11.XCreateWindow.restype = c_ulong
libX11.XDefaultScreen.argtypes = [Display]
libX11.XDefaultScreen.restype = c_int

libX11.XDefaultVisual.argtypes = [Display, c_int]
libX11.XDefaultVisual.restype = c_void_p

libX11.XDefaultDepth.argtypes = [Display, c_int]
libX11.XDefaultDepth.restype = c_int

libX11.XRootWindow.argtypes = [Display, c_int]
libX11.XRootWindow.restype = Window

libX11.XCreateColormap.restype = c_ulong
libX11.XCreateColormap.argtypes = [Display, Window, c_void_p, c_int]

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

libX11.XBlackPixel.argtypes = [Display, c_int]
libX11.XBlackPixel.restype = c_ulong

libX11.XWhitePixel.argtypes = [Display, c_int]
libX11.XWhitePixel.restype = c_ulong

_display = None

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

class XErrorEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("display", ctypes.c_void_p),
        ("resourceid", ctypes.c_ulong),
        ("serial", ctypes.c_ulong),
        ("error_code", ctypes.c_ubyte),
        ("request_code", ctypes.c_ubyte),
        ("minor_code", ctypes.c_ubyte),
    ]
    
libX11.XNextEvent.argtypes = [Display, POINTER(XEvent)]
libX11.XNextEvent.restype = c_int

libX11.XCreateColormap.restype = c_ulong
libX11.XCreateColormap.argtypes = [Display, Window, c_void_p, c_int]

libX11.XMatchVisualInfo.argtypes = [Display, c_int, c_int, c_int, POINTER(XVisualInfo)]
libX11.XMatchVisualInfo.restype = c_int

X_EVENT_MASKS = {
    "KEYPRESS":          (1 << 0),
    "KEYRELEASE":        (1 << 1),
    "BUTTONPRESS":       (1 << 2),
    "BUTTONRELEASE":     (1 << 3),
    "ENTERWINDOW":       (1 << 4),
    "LEAVEWINDOW":       (1 << 5),
    "POINTERMOTION":     (1 << 6),
    "FOCUSCHANGE":       (1 << 8),
    "EXPOSURE":          (1 << 15),
    "STRUCTURE":         (1 << 17),
    "PROPERTYCHANGE":    (1 << 19),
    "VISIBILITY":        (1 << 23),
    "SUBSTRUCTURE":      (1 << 25),
    "COLORMAPCHANGE":    (1 << 29)
}

X_EVENT_MASK = (
    X_EVENT_MASKS["KEYPRESS"] |
    X_EVENT_MASKS["KEYRELEASE"] |
    X_EVENT_MASKS["BUTTONPRESS"] |
    X_EVENT_MASKS["BUTTONRELEASE"] |
    X_EVENT_MASKS["ENTERWINDOW"] |
    X_EVENT_MASKS["LEAVEWINDOW"] |
    X_EVENT_MASKS["POINTERMOTION"] |
    X_EVENT_MASKS["FOCUSCHANGE"] |
    X_EVENT_MASKS["EXPOSURE"] |
    X_EVENT_MASKS["STRUCTURE"] |
    X_EVENT_MASKS["PROPERTYCHANGE"] |
    X_EVENT_MASKS["VISIBILITY"] |
    X_EVENT_MASKS["SUBSTRUCTURE"] |
    X_EVENT_MASKS["COLORMAPCHANGE"]
)

CWBackPixel = 1 << 0
CWBorderPixel = 1 << 3
CWEventMask  = 1 << 11
CWColormap = 1 << 13

VALUEMASK = CWBackPixel | CWBorderPixel | CWEventMask | CWColormap

INPUT_OUTPUT = 1

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(XErrorEvent))
def x_error_handler(error_event_ptr):
    e = error_event_ptr.contents
    print("X Error caught!")
    print(f"Error code: {e.error_code}")
    print(f"Request code: {e.request_code}")
    print(f"Minor code: {e.minor_code}")
    print(f"Resource ID: {hex(e.resourceid)}")
    print(f"Serial: {e.serial}")
    return 0

libX11.XSetErrorHandler(x_error_handler)

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

    if not root:
        raise RuntimeError("Invalid root window!")

    black = libX11.XBlackPixel(display, screen)
    white = libX11.XWhitePixel(display, screen)

    if not flags:
        flags = PIX11Flags(100, 100, width, height, 1, black, white)

    vinfo = XVisualInfo()
    if not libX11.XMatchVisualInfo(display, screen, 24, 4, ctypes.byref(vinfo)):
        raise RuntimeError("No suitable visual found!")

    visual = ctypes.c_void_p(vinfo.visual)
    depth = vinfo.depth

    attrs = XSetWindowAttributes()
    ctypes.memset(ctypes.byref(attrs), 0, ctypes.sizeof(attrs))
    attrs.background_pixel = flags.background
    attrs.border_pixel = flags.border_color
    attrs.event_mask = X_EVENT_MASK

    colormap = libX11.XCreateColormap(display, root, visual, 0)
    attrs.colormap = colormap

    window = libX11.XCreateWindow(
        display,
        root,
        flags.x, flags.y,
        flags.width, flags.height,
        flags.border,
        depth,
        INPUT_OUTPUT,
        visual,
        VALUEMASK,
        ctypes.byref(attrs)
    )

    if not window:
        raise RuntimeError("Failed to create X11 window")

    # Set title, select input, and map window
    libX11.XStoreName(display, window, title.encode("utf-8"))
    libX11.XSelectInput(display, window, X_EVENT_MASK)

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

    if not display:
        # No valid display, probably running headless
        return []

    event = XEvent()
    events = []
    
    try:
        while True:
            pending = libX11.XPending(display)
            if pending <= 0:
                break
            libX11.XNextEvent(display, ctypes.byref(event))
            e_type = event.type
            e = event # shortcut

            # --- Keyboard ---
            if e_type == 2:   # KeyPress
                events.append(PIonEvent("KEYDOWN", keycode=e.xkey.keycode, x=e.xkey.x, y=e.xkey.y))
            elif e_type == 3: # KeyRelease
                events.append(PIonEvent("KEYUP", keycode=e.xkey.keycode, x=e.xkey.x, y=e.xkey.y))

            # --- Mouse Buttons ---
            elif e_type == 4: # ButtonPress
                button = e.xbutton.button
                name = {1: "LEFT_DOWN", 2: "MIDDLE_DOWN", 3: "RIGHT_DOWN"}.get(button, "MOUSEDOWN")
                events.append(PIonEvent(name, button=button, x=e.xbutton.x, y=e.xbutton.y))
            elif e_type == 5: # ButtonRelease
                button = e.xbutton.button
                name = {1: "LEFT_UP", 2: "MIDDLE_UP", 3: "RIGHT_UP"}.get(button, "MOUSEUP")
                events.append(PIonEvent(name, button=button, x=e.xbutton.x, y=e.xbutton.y))

            # --- Motion ---
            elif e_type == 6: # MotionNotify
                events.append(PIonEvent("MOUSEMOVE", x=e.xbutton.x, y=e.xbutton.y))

            # --- Window crossing ---
            elif e_type == 7: # EnterNotify
                events.append(PIonEvent("MOUSEENTER", x=e.xbutton.x, y=e.xbutton.y))
            elif e_type == 8: # LeaveNotify
                events.append(PIonEvent("MOUSELEAVE", x=e.xbutton.x, y=e.xbutton.y))

            # --- Focus ---
            elif e_type == 9: # FocusIn
                events.append(PIonEvent("FOCUS_GAINED"))
            elif e_type == 10: # FocusOut
                events.append(PIonEvent("FOCUS_LOST"))

            # --- Expose / Redraw ---
            elif e_type == 12: # Expose
                events.append(PIonEvent("EXPOSE"))

            # --- Visibility ---
            elif e_type == 15: # VisibilityNotify
                events.append(PIonEvent("REDRAW"))

            # --- Structure / Resize / Move ---
            elif e_type == 22: # ConfigureNotify
                events.append(PIonEvent("RESIZE",
                    x=e.xconfigure.x,
                    y=e.xconfigure.y,
                    width=e.xconfigure.width,
                    height=e.xconfigure.height
                ))

            # --- Map / Unmap / Destroy ---
            elif e_type == 19: # MapNotify
                events.append(PIonEvent("SHOW"))
            elif e_type == 18: # UnmapNotify
                events.append(PIonEvent("HIDE"))
            elif e_type == 17: # DestroyNotify
                events.append(PIonEvent("DESTROY", destroyed=False))

            # --- Client / Close requests ---
            elif e_type == 33: # ClientMessage (e.g., WM_DELETE_WINDOW)
                events.append(PIonEvent("CLOSE", destroyed=False))

            # --- Property changed (like window title, icon, etc.) ---
            elif e_type == 28: # PropertyNotify
                events.append(PIonEvent("PROPERTYCHANGE"))

            # --- MappingNotify (keyboard layout changes) ---
            elif e_type == 34:
                events.append(PIonEvent("INPUTLANGCHANGE"))

            else:
                events.append(PIonEvent("UNKNOWN", raw_type=e_type))
    except Exception as e:
        print("X11 Poll Error:", e)
    return events

def is_window_alive(window_tuple) -> bool:
    display, window = window_tuple
    attrs = XWindowAttributes()
    status = libX11.XGetWindowAttributes(display, window, ctypes.byref(attrs))
    return status != 0

def get_gpu(window_tuple, api:Optional[str]=None, driver:Optional[BaseGPUD]=None) -> GPU_API:
    display, window = window_tuple
    gpu = GPU_API(api, driver)
    return gpu

def attach_gpu(window_tuple, gpu:GPU_API) -> None:
    display, window = window_tuple
    gpu.driver.init(display, window, create_and_attach_ctx=True)