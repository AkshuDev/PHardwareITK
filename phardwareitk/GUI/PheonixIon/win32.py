import ctypes
from ctypes import wintypes
from typing import Optional

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
gdi32 = ctypes.windll.gdi32

from phardwareitk.GUI.PheonixIon.types import *
from phardwareitk.GUI.pheonix_ion import GPU_API, PIonContext
from phardwareitk.Extensions.Windows import *
from phardwareitk.GPU._base import BaseGPUD

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
    # --- Window lifecycle ---
    if msg == WM_CREATE:
        _windows_events.append(PIonEvent("CREATE"))
        return 0
    elif msg == WM_DESTROY:
        _windows_events.append(PIonEvent("QUIT"))
        user32.PostQuitMessage(0)
        return 0
    elif msg == WM_CLOSE:
        _windows_events.append(PIonEvent("CLOSE", destroyed=False))
        return 0
    elif msg == WM_SHOWWINDOW:
        if wparam:  # TRUE means shown
            _windows_events.append(PIonEvent("SHOW"))
        else:
            _windows_events.append(PIonEvent("HIDE"))
        return 0
    elif msg == WM_SIZE:
        width = lparam & 0xFFFF
        height = (lparam >> 16) & 0xFFFF
        size_type = wparam
        if size_type == 1:  # minimized
            _windows_events.append(PIonEvent("MINIMIZE"))
        elif size_type == 2:  # maximized
            _windows_events.append(PIonEvent("MAXIMIZE"))
        elif size_type == 0:  # restored
            _windows_events.append(PIonEvent("RESTORE"))
        _windows_events.append(PIonEvent("RESIZE", width=width, height=height))
        return 0
    elif msg == WM_MOVE:
        x = lparam & 0xFFFF
        y = (lparam >> 16) & 0xFFFF
        _windows_events.append(PIonEvent("MOVE", x=x, y=y))
        return 0

    # --- Mouse ---
    elif msg == WM_MOUSEMOVE:
        x = lparam & 0xFFFF
        y = (lparam >> 16) & 0xFFFF
        _windows_events.append(PIonEvent("MOUSEMOVE", x=x, y=y))
        return 0
    elif msg == WM_LBUTTONDOWN:
        _windows_events.append(PIonEvent("LEFT_DOWN"))
        return 0
    elif msg == WM_LBUTTONUP:
        _windows_events.append(PIonEvent("LEFT_UP"))
        return 0
    elif msg == WM_RBUTTONDOWN:
        _windows_events.append(PIonEvent("RIGHT_DOWN"))
        return 0
    elif msg == WM_RBUTTONUP:
        _windows_events.append(PIonEvent("RIGHT_UP"))
        return 0
    elif msg == WM_MBUTTONDOWN:
        _windows_events.append(PIonEvent("MIDDLE_DOWN"))
        return 0
    elif msg == WM_MBUTTONUP:
        _windows_events.append(PIonEvent("MIDDLE_UP"))
        return 0
    elif msg == WM_MOUSEWHEEL:
        delta = ctypes.c_short((wparam >> 16) & 0xFFFF).value
        _windows_events.append(PIonEvent("SCROLL", delta=delta))
        return 0
    elif msg == WM_MOUSELEAVE:
        _windows_events.append(PIonEvent("MOUSELEAVE"))
        return 0
    elif msg == WM_MOUSEHOVER:
        _windows_events.append(PIonEvent("MOUSEENTER"))
        return 0

    # --- Keyboard ---
    elif msg == WM_KEYDOWN:
        _windows_events.append(PIonEvent("KEYDOWN", keycode=wparam))
        return 0
    elif msg == WM_KEYUP:
        _windows_events.append(PIonEvent("KEYUP", keycode=wparam))
        return 0
    elif msg == WM_CHAR:
        _windows_events.append(PIonEvent("KEYPRESS", char=chr(wparam)))
        return 0
    elif msg == WM_IME_COMPOSITION:
        _windows_events.append(PIonEvent("IME_STARTCOMPOSITION"))
        return 0
    elif msg == WM_IME_ENDCOMPOSITION:
        _windows_events.append(PIonEvent("IME_ENDCOMPOSITION"))
        return 0

    # --- Other / system ---
    elif msg == WM_DISPLAYCHANGE:
        _windows_events.append(PIonEvent("DISPLAYCHANGE"))
        return 0
    elif msg == WM_POWERBROADCAST:
        _windows_events.append(PIonEvent("POWERBROADCAST"))
        return 0
    elif msg == WM_TIMER:
        _windows_events.append(PIonEvent("TIMER", timer_id=wparam))
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
    wndclass.style = CS_HREDRAW | CS_VREDRAW | CS_OWNDC
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

def get_gpu(hwnd: HWND, api: Optional[str], driver: Optional[BaseGPUD]) -> GPU_API:
    if not hwnd:
        raise RuntimeError("Cannot create context for a invalid window!")

    gpu = GPU_API(api, driver)
    gpu.driver.init(None, hwnd, create_and_attach_ctx=False)
    return gpu

def attach_gpu(hwnd: HWND, gpu: GPU_API) -> PIonContext:
    return gpu.driver.create_context(None, hwnd)