import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

from phardwareitk.GUI.PheonixIon.types import *
from phardwareitk.Extensions.Windows import *

WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, HWND, UINT, WPARAM, LPARAM)
_windows_events = []

class PIWin32Flags:
    def __init__(self, exStyle:int=0, className="PheonixIonWindow", windowName="Pheonix Ion", style:int=WS_OVERLAPPEDWINDOW, x:int=100, y:int=100, width:int=800, height:int=600, parent:Optional[HWND]=None, menu:Optional[HMENU]=None, instance:Optional[HINSTANCE]=None, param:Optional[LPVOID]=None) -> None:
        self.exStyle = exStyle
        self.className = className
        self.windowName = windowName
        self.style = style
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.parent = parent
        self.menu = menu
        self.instance = instance if instance else kernel32.GetModuleHandleW(None)
        self.param = param

    def to_c(self):
        return (self.exStyle, self.className, self.windowName, self.style, self.x, self.y, self.width, self.height, self.parent, self.menu, self.instance, self.param)

def _wnd_proc(hwnd, msg, wparam, lparam):
    global _windows_events
    if msg == WM_DESTROY:
        _windows_events.append({"type": "QUIT"})
        return 0
    elif msg == WM_CLOSE:
        _windows_events.append({"type": "CLOSE"})
        return 0
    return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

def create_window(title:str="Pheonix Ion", width:int=800, height:int=600, flags:PIWin32Flags=None) -> HWND:
    """Create a Win32 window and return its handle."""
    hInstance = kernel32.GetModuleHandleW(None)
    className = "PheonixIonWindow"

    # Register class
    wndclass = wintypes.WNDCLASS()
    wndclass.lpfnWndProc = WNDPROC(_wnd_proc)
    wndclass.hInstance = hInstance
    wndclass.lpszClassName = className
    user32.RegisterClassW(ctypes.byref(wndclass))

    if not flags:
        flags = PIWin32Flags(0, className, title, WS_OVERLAPPEDWINDOW, 100, 100, width, height, None, None, hInstance, None)

    hwnd = user32.CreateWindowExW(*flags.to_c())
    return hwnd

def show_window(hwnd:HWND) -> None:
    user32.ShowWindow(hwnd, 1)
    user32.UpdateWindow(hwnd)

def poll_events(hwnd):
    import ctypes
    msg = wintypes.MSG()
    events = _windows_events.copy()
    _windows_events.clear()
    while user32.PeekMessageW(ctypes.byref(msg), hwnd, 0, 0, 1):
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))
    return events