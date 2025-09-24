"""GUI Library, from PHardwareITK itself"""

import platform
import os
import sys
import ctypes

from typing import *

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

class GPUContext:
    def __init__(self, window, api:str=None) -> None:
        self.window = window
        self.api = api or self._detect_best_api()
        self.context_handle = None
        self.init_context()

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

    def _init_vulkan(self):
        # Placeholder for Vulkan context initialization
        self.context_handle = "VulkanContextHandle"

    def _init_opengl(self):
        # Placeholder for OpenGL context initialization
        self.context_handle = "OpenGLContextHandle"

    def _init_directx(self):
        # Placeholder for DirectX context initialization
        self.context_handle = "DirectXContextHandle"

    def _init_metal(self):
        # Placeholder for Metal context initialization
        self.context_handle = "MetalContextHandle"

    def _init_opengl_es(self):
        # Placeholder for OpenGL ES context initialization
        self.context_handle = "OpenGLESContextHandle"

    def init_context(self):
        if self.api == "Vulkan":
            self._init_vulkan()
        elif self.api == "OpenGL":
            self._init_opengl()
        elif self.api == "DirectX":
            self._init_directx()
        elif self.api == "Metal":
            self._init_metal()
        elif self.api == "OpenGL ES":
            self._init_opengl_es()
        else:
            raise NoCompatibleGraphicsAPIFound(f"Unsupported graphics API: {self.api}")

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

    def poll_events(self, win:Union[int, PIonWindow]):
        """Poll events for the created window.
        
        Parameters:
            win (int | PIonWindow): The window index or the PIonWindow class instance"""
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

    def get_native_handle(self, win:Union[int, PIonWindow]):
        """Return OS-specific window handle (HWND on Win, X11 tuple, NSWindow on Mac)."""
        handle = self.get_window(win)
        if not handle: return None

        return handle.handle