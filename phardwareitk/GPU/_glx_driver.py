import ctypes
from ctypes import *
from typing import Any, Optional

from ._base import BaseGPUD
import platform

class UnsupportedPlatform(Exception):
    def __init__(self, message="Unsupported platform for window creation"):
        super().__init__(message)

class GLXDriver(BaseGPUD):
    def __init__(self, libGL: Optional[str]=None, screen: Optional[int]=None):
        """Initialization
        
        Args:
            libGL (Optional, str): The path to the OpenGL Library, if None this class automatically tries to get it based on OS. Defaults to None
            screen (Optional, c_int): The screen to use, if None this class tries to get it based on the OS, Defaults to None."""
        self.display = None
        self.window = None
        self.ctx = None
        self.platform = platform.system().lower()
        if libGL is not None:
            self.libGL = cdll.LoadLibrary(libGL)
        else:
            if self.platform == "linux":
                self.libGL = cdll.LoadLibrary("libGL.so.1")
            elif self.platform == "freebsd":
                self.libGL = cdll.LoadLibrary("libGL.so")
            elif self.platform == "openbsd":
                self.libGL = cdll.LoadLibrary("libGL.so")
            elif self.platform == "netbsd":
                self.libGL = cdll.LoadLibrary("libGL.so")
            elif self.platform == "windows":
                self.libGL = cdll.LoadLibrary("opengl32.dll")
            elif self.platform == "darwin":
                self.libGL = cdll.LoadLibrary("/System/Library/Frameworks/OpenGL.framework/OpenGL")
            else:
                raise UnsupportedPlatform(f"Unsupported OS for GLX/OpenGL: {self.platform}, try passing lib path manually?")
        self.screen = screen

    def init(self, display, window):
        """Initialize GLX"""
        self.display = display
        self.window = window

        # Set all the args and return types
        self.libGL.glXChooseVisual.argtypes = [c_void_p, c_int, POINTER(c_int)]
        self.libGL.glXChooseVisual.restype = c_void_p

        self.libGL.glXCreateContext.argtypes = [c_void_p, c_void_p, c_void_p, c_int]
        self.libGL.glXCreateContext.restype = c_void_p

        self.libGL.glXMakeCurrent.argtypes = [c_void_p, c_ulong, c_void_p]
        self.libGL.glXMakeCurrent.restype = c_int

        self.libGL.glXSwapBuffers.argtypes = [c_void_p, c_uint64]
        self.libGL.glXSwapBuffers.restype = c_void_p

        self.libGL.glClearColor.argtypes = [c_float, c_float, c_float, c_float]
        self.libGL.glClearColor.restype = c_void_p

        self.libGL.glXDestroyContext.argtypes = [c_void_p, c_void_p]
        self.libGL.glXDestroyContext.restype = c_void_p

        self.libGL.glXGetProcAddress.argtypes = [c_char_p]
        self.libGL.glXGetProcAddress.restype = c_void_p

        screen: Union[c_int, int] = self.screen if self.screen is not None else None
        if self.screen is None:
            if self.platform == "linux":
                screen = cdll.LoadLibrary("libX11.so.6").XDefaultScreen(display)
            else:
                raise UnsupportedPlatform("This is an unimplemented operating system, please consider manually passing the screen!")
        attribs = (c_int * 5)(0x8010, 1, 0x8011, 1, 0) # GLX_RGBA, GLX_DOUBLEBUFFER, NULL
        visual = self.libGL.glXChooseVisual(display, screen, attribs)
        self.ctx = self.libGL.glXCreateContext(display, visual, None, True)

        if not self.ctx:
            raise RuntimeError("Failed to create GLX Context!")
        
        if self.libGL.glXMakeCurrent(display, window, self.ctx) == 0:
            raise RuntimeError("glXMakeCurrent failed!")
        
        self.libGL.glClearColor(0.0, 0.0, 0.0, 1.0)

    def clear(self, r: int, g: int, b: int, a: int):
        """Clear the screen with the specified colors (red, green, blue, alpha)"""
        r = r / 100
        g = g / 100
        b = b / 100
        a = a / 100
        self.libGL.glClearColor(r, g, b, a)
    
    def swap(self):
        """Swap buffers"""
        self.libGL.glXSwapBuffers(self.display, self.window)

    def shutdown(self):
        """Delete the context and deinitialize GLX"""
        if self.ctx:
            self.libGL.glXDestroyContext(self.display, self.ctx)

    def load_function(self, name: str) -> c_void_p:
        """Loads the specified function"""
        addr = self.libGL.glXGetProcAddress(name.encode())
        if not addr:
            raise RuntimeError(f"Function {name} not found in GL driver")
        return addr