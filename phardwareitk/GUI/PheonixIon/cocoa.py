import ctypes

objc = ctypes.cdll.LoadLibrary("/usr/lib/libobjc.A.dylib")
AppKit = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/AppKit.framework/AppKit")

# Objective-C runtime helpers
objc.objc_getClass.restype = ctypes.c_void_p
objc.sel_registerName.restype = ctypes.c_void_p

def get_class(name: str):
    return objc.objc_getClass(name.encode("utf-8"))

def get_selector(name: str):
    return objc.sel_registerName(name.encode("utf-8"))

def send_msg(receiver, selector, *args, restype=ctypes.c_void_p, argtypes=None):
    objc.objc_msgSend.restype = restype
    if argtypes:
        objc.objc_msgSend.argtypes = argtypes
    return objc.objc_msgSend(receiver, selector, *args)

class PICocoaFlags:
    def __init__(self, width=800, height=600, title="Pheonix Ion"):
        self.width = width
        self.height = height
        self.title = title

def create_window(title: str="Pheonix Ion", width:int=800, height:int=600, flags:PICocoaFlags=None):
    if not flags:
        flags = PICocoaFlags(width, height, title)

    NSApplication = get_class("NSApplication")
    shared_app = send_msg(NSApplication, get_selector("sharedApplication"))

    NSWindow = get_class("NSWindow")
    style_mask = 15  # titled, closable, resizable
    rect = (0.0, 0.0, float(flags.width), float(flags.height))

    # Create window (super simplified!)
    window = send_msg(NSWindow, get_selector("alloc"))
    window = send_msg(window, get_selector("initWithContentRect:styleMask:backing:defer:"),
                      rect, style_mask, 2, False)

    send_msg(window, get_selector("setTitle:"), flags.title.encode("utf-8"))
    send_msg(window, get_selector("makeKeyAndOrderFront:"), None)

    return window

def show_window(window):
    # Already visible after creation
    return None

def poll_events(window):
    # Stub: Cocoa runs an event loop
    return []
