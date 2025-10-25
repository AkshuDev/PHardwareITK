import ctypes
from ctypes import *
from typing import Any, Optional

from phardwareitk.GUI.pheonix_ion import PIonContext

from ._base import BaseGPUD
import platform

class UnsupportedPlatform(Exception):
    def __init__(self, message="Unsupported platform for window creation"):
        super().__init__(message)

class GLDriver(BaseGPUD):
    """Cross Platform OpenGL Driver"""
    def __init__(self, libGL: Optional[str]=None, screen: Optional[int]=None):
        """Initialization
        
        Args:
            libGL (Optional, str): The path to the OpenGL Library, if None this class automatically tries to get it based on OS. Defaults to None
            screen (Optional, c_int): The screen to use, if None this class tries to get it based on the OS, Defaults to None."""
        self.display = None
        self.window = None
        self.ctx = None
        self.platform = platform.system().lower()
        self.lib_path = ""
        self.win32 = None
        self.user32 = None
        self.gdi32 = None
        self.hdc = None
        if self.platform == "windows":
            from ctypes import wintypes as win
            self.win32 = win

        if libGL is not None:
            self.libGL = cdll.LoadLibrary(libGL)
            self.lib_path = libGL
        else:
            if self.platform == "linux":
                self.libGL = cdll.LoadLibrary("libGL.so.1")
                self.lib_path = "libGL.so.1"
            elif self.platform == "freebsd":
                self.libGL = cdll.LoadLibrary("libGL.so")
                self.lib_path = "libGL.so"
                self.platform = "linux"
            elif self.platform == "openbsd":
                self.libGL = cdll.LoadLibrary("libGL.so")
                self.lib_path = "libGL.so"
                self.platform = "linux"
            elif self.platform == "netbsd":
                self.libGL = cdll.LoadLibrary("libGL.so")
                self.lib_path = "libGL.so"
                self.platform = "linux"
            elif self.platform == "windows":
                self.libGL = cdll.LoadLibrary("opengl32.dll")
                self.lib_path = "opengl32.dll"
            elif self.platform == "darwin":
                self.libGL = cdll.LoadLibrary("/System/Library/Frameworks/OpenGL.framework/OpenGL")
                self.lib_path = "/System/Library/Frameworks/OpenGL.framework/OpenGL"
            else:
                raise UnsupportedPlatform(f"Unsupported OS for GLX/OpenGL: {self.platform}, try passing lib path manually?")
        self.screen = screen

    def init(self, display: Any, window: Any, create_and_attach_ctx: bool=False):
        if self.platform == "linux":
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

            if create_and_attach_ctx:
                return self.create_context(display, window)
                
        elif self.platform == "windows":
            self.window = window # display is useless

            self.gdi32 = ctypes.windll.gdi32
            self.user32 = ctypes.windll.user32

            self.libGL.glClearColor.argtypes = [c_float, c_float, c_float, c_float]
            self.libGL.glClearColor.restype = None
            self.libGL.glClear.argtypes = [c_int]
            self.libGL.glClear.restype = None
            
            if not self.hdc:
                self.hdc = self.user32.GetDC(window)

            if create_and_attach_ctx:
                return self.create_context(display, window)

    def clear(self, r: int, g: int, b: int, a: int):
        r = r / 100
        g = g / 100
        b = b / 100
        a = a / 100
        self.libGL.glClearColor(r, g, b, a)
        self.libGL.glClear(0x00004000) # GL_COLOR_BUFFER_BIT
    
    def swap(self):
        if self.platform == "linux":
            self.libGL.glXSwapBuffers(self.display, self.window)
        elif self.platform == "windows":
            self.gdi32.SwapBuffers(self.hdc)

    def shutdown(self):
        self.destroy_context()

    def load_function(self, name: str) -> c_void_p:
        addr = None
        if self.platform == "linux":
            addr = self.libGL.glXGetProcAddress(name.encode())
        elif self.platform == "windows":
            pass
        if not addr:
            raise RuntimeError(f"Function {name} not found in GL driver")
        return addr
    
    def destroy_context(self):
        if self.ctx:
            if self.platform == "linux":
                self.libGL.glXDestroyContext(self.display, self.ctx)
            elif self.platform == "windows":
                if self.ctx:
                    self.libGL.wglDeleteContext(self.ctx)
                    self.ctx = None
                if self.hdc:
                    self.user32.ReleaseDC(self.ctx, self.hdc)
                    self.hdc = None
    
    def create_context(self, display, window):
        if self.platform == "linux":
            if self.ctx:
                self.destroy_context()

            attribs = (c_int * 5)(0x8010, 1, 0x8011, 1, 0)
            visual = self.libGL.glXChooseVisual(display, 0, attribs)
            self.ctx = self.libGL.glXCreateContext(display, visual, None, True)

            if not self.ctx:
                raise RuntimeError("Failed to create GLX Context")
            
            return PIonContext(
                api_name="OpenGL",
                native_handle={
                    "display": display,
                    "window": window,
                    "glx_context": self.ctx,
                    "visual": visual
                },
                lib_path=self.lib_path,
                metadata={
                    "type": "GLX"
                }
            )
        elif self.platform == "windows":
            class PIXELFORMATDESCRIPTOR(ctypes.Structure):
                _fields_ = [
                    ("nSize", ctypes.c_ushort),
                    ("nVersion", ctypes.c_ushort),
                    ("dwFlags", ctypes.c_uint),
                    ("iPixelType", ctypes.c_ubyte),
                    ("cColorBits", ctypes.c_ubyte),
                    ("cRedBits", ctypes.c_ubyte),
                    ("cRedShift", ctypes.c_ubyte),
                    ("cGreenBits", ctypes.c_ubyte),
                    ("cGreenShift", ctypes.c_ubyte),
                    ("cBlueBits", ctypes.c_ubyte),
                    ("cBlueShift", ctypes.c_ubyte),
                    ("cAlphaBits", ctypes.c_ubyte),
                    ("cAlphaShift", ctypes.c_ubyte),
                    ("cAccumBits", ctypes.c_ubyte),
                    ("cAccumRedBits", ctypes.c_ubyte),
                    ("cAccumGreenBits", ctypes.c_ubyte),
                    ("cAccumBlueBits", ctypes.c_ubyte),
                    ("cAccumAlphaBits", ctypes.c_ubyte),
                    ("cDepthBits", ctypes.c_ubyte),
                    ("cStencilBits", ctypes.c_ubyte),
                    ("cAuxBuffers", ctypes.c_ubyte),
                    ("iLayerType", ctypes.c_ubyte),
                    ("bReserved", ctypes.c_ubyte),
                    ("dwLayerMask", ctypes.c_uint),
                    ("dwVisibleMask", ctypes.c_uint),
                    ("dwDamageMask", ctypes.c_uint)
                ]
            pfd = PIXELFORMATDESCRIPTOR()
            pfd.nSize = ctypes.sizeof(PIXELFORMATDESCRIPTOR)
            pfd.nVersion = 1
            pfd.dwFlags = 0x00000004 | 0x00000020  # PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL
            pfd.iPixelType = 0  # PFD_TYPE_RGBA
            pfd.cColorBits = 32
            pfd.cDepthBits = 24
            pfd.cStencilBits = 8
            pfd.iLayerType = 0  # PFD_MAIN_PLANE

            fmt = self.gdi32.ChoosePixelFormat(self.hdc, ctypes.byref(pfd))
            self.gdi32.SetPixelFormat(self.hdc, fmt, ctypes.byref(pfd))

            # Create OpenGL rendering context
            self.ctx = self.libGL.wglCreateContext(self.hdc)
            self.libGL.wglMakeCurrent(self.hdc, self.ctx)

            return PIonContext(
                api_name="OpenGL",
                native_handle={
                    "hwnd": self.window,
                    "hdc": self.hdc,
                    "hglrc": self.ctx
                },
                lib_path="opengl32.dll",
                metadata={"type": "WGL"}
            )