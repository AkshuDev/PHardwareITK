"""GUI Library, from PHardwareITK itself"""

import platform
import os
import sys
import ctypes

from typing import *

from phardwareitk.GPU._base import BaseGPUD
from phardwareitk.GUI.PheonixIon.types import *

class NoCompatibleGraphicsAPIFound(Exception):
    def __init__(self, message="No compatible graphics API found"):
        super().__init__(message)
class UnsupportedPlatform(Exception):
    def __init__(self, message="Unsupported platform for window creation"):
        super().__init__(message)

SYSTEM = platform.system().lower()

def try_load_library(lib_names:list):
    """Try to load a list of library names; return first that succeeds."""
    for name in lib_names:
        try:
            return ctypes.CDLL(name)
        except OSError:
            continue
    return None

class PIonWindow:
    """A Pheonix Ion Window Instance"""
    def __init__(self, title:str, width:int, height:int, flags=None, handle=None) -> None:
        self.title = title
        self.width = width
        self.height = height
        self.handle = handle

        self.backends = PIenum()
        self.backends.create_enum(["Win32", "X11", "Cocoa"], 1)
        self.backend = self._select_backend()

        self.flags = flags

    def _select_backend(self, backend:Union[str, PIenum]=None) -> str:
        if not backend:
            if SYSTEM == "windows":
                return self.backends.access("Win32")
            elif SYSTEM == "linux":
                return self.backends.access("X11")
            elif SYSTEM == "darwin":
                return self.backends.access("Cocoa")
            else:
                print("Unknown platform for automatic backend selection!, please specify backend manually.")
                return None
        else:
            if isinstance(backend, str):
                bkend = self.backends.access(backend)
                if bkend == None:
                    raise UnsupportedPlatform(f"Unsupported backend: {backend}")
                return bkend
            elif isinstance(backend, PIenum):
                return backend.value
            else:
                raise ValueError("Backend must be a string or PIenum instance")

class GPU_API:
    """Pheonix Ion GPU API, use the driver attribute to access functions like -
    ```python
        mygpu = GPU_API() # This is a simplification, the PheonixIon Class will return the GPU_API initialized.
        # Initialize
        mygpu.driver.init(mydisplay, mywin)
        # Clear screen
        mygpu.driver.clear(255, 0, 0, 255) # rgba
        # Destroy
        mygpu.driver.shutdown()
    ```
    """
    def __init__(self, api:str=None, driver:Any=None) -> None:
        self.api = api if api is not None else self._detect_best_api()
        self.available_api = self._get_available_apis()
        self.context_handle = None
        from phardwareitk.GPU._base import BaseGPUD
        self.driver: BaseGPUD = None

        if driver is None:
            for api in self.available_api:
                if api.lower() == "opengl":
                    from phardwareitk.GPU._gl_driver import GLDriver as _driver
                    self.driver = _driver()
                    if not api == self.api:
                        self.api = api
                    break

            else:
                raise NoCompatibleGraphicsAPIFound(f"no {self.available_api} graphics drivers found in phardwareitk, try implementing your own?")
        else:
            self.driver = driver

    def _detect_best_api(self) -> str:
        if self._is_vulkan_available():
            return "Vulkan"
        elif self._opengl_available():
            return "OpenGL"
        elif self._is_directx_available():
            return "DirectX"
        elif self._is_metal_available():
            return "Metal"
        elif self._is_opengl_es_available():
            return "OpenGL ES"
        else:
            raise NoCompatibleGraphicsAPIFound("No compatible graphics API found on this system.")

    def _get_available_apis(self) -> str:
        avail = []
        if self._is_vulkan_available():
            avail.append("Vulkan")
        if self._opengl_available():
            avail.append("OpenGL")
        if self._is_directx_available():
            avail.append("DirectX")
        if self._is_metal_available():
            avail.append("Metal")
        if self._is_opengl_es_available():
            avail.append("OpenGL ES")
        return avail

    def _is_vulkan_available(self) -> bool:
        if SYSTEM == "windows":
            return try_load_library(["vulkan-1.dll"]) is not None
        elif SYSTEM == "linux":
            return try_load_library(["libvulkan.so.1", "libvulkan.so"]) is not None
        elif SYSTEM == "darwin":
            return False  # Vulkan requires MoltenVK on macOS; assume false for now
        return False

    def _opengl_available(self) -> bool:
        if SYSTEM == "windows":
            return try_load_library(["opengl32.dll"]) is not None
        elif SYSTEM == "linux":
            return try_load_library(["libGL.so.1", "libGL.so"]) is not None
        elif SYSTEM == "darwin":
            return try_load_library(["/System/Library/Frameworks/OpenGL.framework/OpenGL"]) is not None
        return False

    def _is_directx_available(self) -> bool:
        if SYSTEM == "windows":
            return try_load_library(["d3d11.dll", "d3d12.dll"]) is not None
        return False

    def _is_metal_available(self) -> bool:
        # Placeholder for actual Metal detection logic
        return SYSTEM == "darwin"

    def _is_opengl_es_available(self) -> bool:
        if SYSTEM == "windows":
            return try_load_library(["libGLESv2.dll"]) is not None
        elif SYSTEM == "linux":
            return try_load_library(["libGLESv2.so"]) is not None
        elif SYSTEM == "darwin":
            return try_load_library(["/System/Library/Frameworks/OpenGLES.framework/OpenGLES"]) is not None
        return False

class PIonContext:
    def __init__(self, api_name: str, native_handle: object, lib_path: str, metadata: dict = None):
        self.api_name = api_name # e.g., "OpenGL", "Vulkan", "DirectX", "Metal"
        self.native_handle = native_handle # platform-specific (X11, HWND, Android Surface)
        self.lib_path = lib_path # path to the lib
        self.metadata = metadata or {} # optional: version, extensions, etc.

class PheonixIon:
    def __init__(self):
        self.system:str = SYSTEM
        self.windows:list[PIonWindow] = []

        self.pionbackend = None
        self.backend = ""

        self._load_backend()

    def _load_backend(self, backend__:str=None):
        if backend__:
            backend_ = backend__.lower()
            if backend_ == "win32":
                from phardwareitk.GUI.PheonixIon import win32 as backend
                self.pionbackend = backend
                self.backend = "Win32"
            elif backend_ == "x11":
                from phardwareitk.GUI.PheonixIon import x11 as backend
                self.pionbackend = backend
                self.backend = "X11"
            elif backend_ == "cacoa":
                from phardwareitk.GUI.PheonixIon import cacao as backend
                self.pionbackend = backend
                self.backend = "Cacoa"
            else:
                raise UnsupportedPlatform(f"Unknown backend: {backend__}")

            return None

        if self.system == "windows":
            from phardwareitk.GUI.PheonixIon import win32 as backend
            self.pionbackend = backend
            self.backend = "Win32"
        elif self.system == "linux":
            from phardwareitk.GUI.PheonixIon import x11 as backend
            self.pionbackend = backend
            self.backend = "X11"
        elif self.system == "darwin":
            from phardwareitk.GUI.PheonixIon import cocoa as backend
            self.pionbackend = backend
            self.backend = "Cacoa"
        else:
            raise UnsupportedPlatform(f"Unsupported platform: {self.system}")
        return None

    def create_window(self, title:str="Pheonix Ion", width:int=800, height:int=600, flags=None) -> PIonWindow:
        """Create a window with specified parameters.
        Parameters:
            title (str): Title of the window.
            width (int): Width of the window.
            height (int): Height of the window.
            backend (str or PIenum): Backend to use for window creation. If None, auto-detects based on platform.
            flags: Additional flags for window creation (backend-specific), For example PIWin32Flags for Win32 backend.
        Returns:
            PIonWindow: The created window object.
        """
        handle = self.pionbackend.create_window(title, width, height, flags)

        win = PIonWindow(title, width, height, flags, handle)
        win._select_backend(self.backend)

        self.windows.append(win)

        return win

    def poll_events(self, win:Union[int, PIonWindow]) -> list:
        """Poll events for the created window.
        
        Parameters:
            win (int | PIonWindow): The window index or the PIonWindow class instance
            
        Returns:
            list: A List of PIonEvent from PheonixIon.types"""
        handle = self.get_native_handle(win)

        if not handle:
            return []

        return self.pionbackend.poll_events(handle)

    def destroy_window(self, win: Union[int, PIonWindow]):
        """
        Destroy a window and release its resources.

        Parameters:
            win (int | PIonWindow): Window index or PIonWindow instance.
        """
        window = self.get_native_handle(win)
        if not window:
            return
        self.pionbackend.destroy_window(window)
        self.windows = [w for w in self.windows if w.handle != window]

    def hide_window(self, win: Union[int, PIonWindow]):
        """
        Hide a window (make it invisible but not destroyed).

        Parameters:
            win (int | PIonWindow): Window index or PIonWindow instance.
        """
        window = self.get_native_handle(win)
        if window:
            self.pionbackend.hide_window(window)

    def show_window(self, win: Union[int, PIonWindow]):
        """
        Show a previously hidden window.

        Parameters:
            win (int | PIonWindow): Window index or PIonWindow instance.
        """
        window = self.get_native_handle(win)
        if window:
            self.pionbackend.show_window(window)

    def set_window_title(self, win: Union[int, PIonWindow], title: str):
        """
        Change the title of a window.

        Parameters:
            win (int | PIonWindow): Window index or PIonWindow instance.
            title (str): New window title.
        """
        window = self.get_native_handle(win)
        if window:
            self.pionbackend.set_window_title(window, title)
            w = self.get_window(win)
            if w:
                w.title = title

    def is_window_alive(self, win: Union[int, PIonWindow]) -> bool:
        """
        Check if a window is still alive (not closed/destroyed).

        Parameters:
            win (int | PIonWindow): Window index or PIonWindow instance.

        Returns:
            bool: True if the window is alive, False otherwise.
        """
        window = self.get_native_handle(win)
        if window:
            return self.pionbackend.is_window_alive(window)
        return False

    def get_window(self, win:Union[int, PIonWindow], throw_err=False) -> Optional[PIonWindow]:
        """Gets the PIonWindow based of its index, or class"""
        if isinstance(win, int):
            return self.windows[win]
        elif isinstance(win, PIonWindow):
            return win
        else:
            if throw_err: raise ValueError("Unknown type provided for parameter 'win', supported types are - int or PIonWindow")
            return None

    def get_native_handle(self, win:Union[int, PIonWindow]) -> Any:
        """Return OS-specific window handle (HWND on Win, X11 tuple, NSWindow on Mac)."""
        handle = self.get_window(win)
        if not handle: return None

        return handle.handle
    
    def get_gpu(self, win:Union[int, PIonWindow], api:Optional[str]=None, driver:Optional[BaseGPUD]=None) -> Optional[GPU_API]:
        """Returns the GPU context in form of GPU_API class"""
        window = self.get_native_handle(win)
        if window:
            return self.pionbackend.get_gpu(window, api, driver)
        return None
    
    def attach_gpu(self, win:Union[int, PIonWindow], gpu:GPU_API) -> None:
        window = self.get_native_handle(win)
        if window:
            return self.pionbackend.attach_gpu(window, gpu)
        return None
    