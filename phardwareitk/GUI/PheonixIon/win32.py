import ctypes
from ctypes import wintypes
from typing import Optional

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
gdi32 = ctypes.windll.gdi32

from phardwareitk.GUI.PheonixIon.types import *
from phardwareitk.Extensions.Windows import *

user32.DefWindowProcW.argtypes = [HWND, UINT, WPARAM, LPARAM]
user32.DefWindowProcW.restype  = LRESULT
user32.PeekMessageW.argtypes = [ctypes.POINTER(MSG), HWND, UINT, UINT, UINT]
user32.PeekMessageW.restype  = BOOL
user32.TranslateMessage.argtypes = [ctypes.POINTER(MSG)]
user32.TranslateMessage.restype  = BOOL
user32.DispatchMessageW.argtypes = [ctypes.POINTER(MSG)]
user32.DispatchMessageW.restype  = LRESULT

gdi32.GetStockObject.restype = HGDIOBJ
gdi32.GetStockObject.argtypes = [ctypes.c_int]

_windows_events = []

class PIWin32Flags:
    def __init__(
        self,
        exStyle: int = 0,
        className="PheonixIonWindow",
        windowName="Pheonix Ion",
        style: int = WS_OVERLAPPEDWINDOW,
        x: int = 100,
        y: int = 100,
        width: int = 800,
        height: int = 600,
        parent: Optional[HWND] = None,
        menu: Optional[HMENU] = None,
        instance: Optional[HINSTANCE] = None,
        param: Optional[LPVOID] = None,
    ) -> None:
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
        return (
            self.exStyle,
            self.className,
            self.windowName,
            self.style,
            self.x,
            self.y,
            self.width,
            self.height,
            self.parent,
            self.menu,
            self.instance,
            self.param,
        )


def _wnd_proc(hwnd, msg, wparam, lparam):
    global _windows_events
    if msg == WM_DESTROY:
        _windows_events.append(PIonEvent("QUIT"))
        user32.PostQuitMessage(0)
        return 0
    elif msg == WM_CLOSE:
        _windows_events.append(PIonEvent("CLOSE"))
        user32.DestroyWindow(hwnd)
        return 0
    return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

_wnd_proc_callback = WNDPROC(_wnd_proc)

def create_window(
    title: str = "Pheonix Ion",
    width: int = 800,
    height: int = 600,
    flags: PIWin32Flags = None,
) -> HWND:
    """Create a Win32 window and return its handle."""
    hInstance = kernel32.GetModuleHandleW(None)
    className = "PheonixIonWindow"

    # Register class
    wndclass = WNDCLASS()
    wndclass.style = CS_HREDRAW | CS_VREDRAW
    wndclass.lpfnWndProc = _wnd_proc_callback
    wndclass.cbClsExtra = 0
    wndclass.cbWndExtra = 0
    wndclass.hInstance = hInstance
    wndclass.hIcon = user32.LoadIconW(None, IDI_APPLICATION)
    wndclass.hCursor = user32.LoadCursorW(None, IDC_ARROW)
    wndclass.hbrBackground = gdi32.GetStockObject(WHITE_BRUSH)
    wndclass.lpszMenuName = None
    wndclass.lpszClassName = className

    if not flags:
        flags = PIWin32Flags(
            0,
            className,
            title,
            WS_OVERLAPPEDWINDOW,
            100,
            100,
            width,
            height,
            None,
            None,
            hInstance,
            None,
        )

    if not user32.RegisterClassW(ctypes.byref(wndclass)):
        raise ctypes.WinError()

    hwnd = user32.CreateWindowExW(*flags.to_c())
    return hwnd


def show_window(hwnd: HWND) -> None:
    user32.ShowWindow(hwnd, 1)
    user32.UpdateWindow(hwnd)


def hide_window(hwnd: HWND) -> None:
    user32.ShowWindow(hwnd, 0)
    user32.UpdateWindow(hwnd)


def set_window_title(hwnd: HWND, title: str) -> None:
    user32.SetWindowTextW(hwnd, title)


def destroy_window(hwnd: HWND) -> None:
    user32.DestroyWindow(hwnd)


def poll_events(hwnd: HWND):
    msg = MSG()
    ctypes.memset(ctypes.byref(msg), 0, ctypes.sizeof(msg))
    events = _windows_events.copy()
    _windows_events.clear()
    while user32.PeekMessageW(ctypes.byref(msg), hwnd, 0, 0, 1):
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))
    return events


def is_window_alive(hwnd: HWND) -> bool:
    return user32.IsWindow(hwnd) != 0
