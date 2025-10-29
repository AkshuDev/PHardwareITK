"""OpenGL Driver implementation using BaseGPUD class"""

import ctypes
from ctypes import *
import sys
from typing import Any, Optional

from phardwareitk.GUI.pheonix_ion import PIonContext

from ._base import BaseGPUD
import platform

GL_COLOR_BUFFER_BIT = 0x00004000
GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_INFO_LOG_LENGTH = 0x8B84
GL_ARRAY_BUFFER = 0x8892
GL_STATIC_DRAW = 0x88E4
GL_TEXTURE_2D = 0x0DE1
GL_RGBA = 0x1908
GL_UNSIGNED_BYTE = 0x1401
GL_FRAMEBUFFER = 0x8D40
GL_VERTEX_SHADER = 0x8B31
GL_FRAGMENT_SHADER = 0x8B30

# Pixel format flags for Windows
PFD_DRAW_TO_WINDOW = 0x00000004
PFD_SUPPORT_OPENGL = 0x00000020
PFD_DOUBLEBUFFER = 0x00000001
PFD_TYPE_RGBA = 0
PFD_MAIN_PLANE = 0

FuncType = CFUNCTYPE
if sys.platform.startswith("win"):
    from ctypes import WINFUNCTYPE
    FuncType = WINFUNCTYPE

class UnsupportedPlatform(Exception):
    def __init__(self, message="Unsupported platform for window creation"):
        super().__init__(message)

class GLFunctions:
    """Wrapper for OpenGL functions — dynamically loads and binds symbols."""
    def __init__(self, driver):
        self._driver = driver
        self._lib = driver.lib

    def _get_proc_address(self, name: str, restype=None, argtypes: list=[]):
        """Use the driver's loader to resolve function addresses."""
        return self._driver.load_function(name, restype, argtypes)

    def _bind(self, name: str, restype=None, argtypes: list=[]):
        """Bind a GL function by name with argtypes/restype."""
        fn = self._get_proc_address(name, restype, argtypes)
        if not fn:
            raise RuntimeError(f"Failed to load GL function: {name}")
        
        setattr(self, name, fn)
        return fn

    def _load_gl_functions_common(self):
        """Load core GL 2.0+ functions required by GLDriver"""

        # Tell me which looks better as titles -
        # This is a title
        # ==== OR ====
        # --- This is a title ---

        # Shaders
        self.glCreateShader = self._bind("glCreateShader", c_uint, [c_uint])
        self.glShaderSource = self._bind("glShaderSource", None, [c_uint, c_int, POINTER(c_char_p), POINTER(c_int)])
        self.glCompileShader = self._bind("glCompileShader", None, [c_uint])
        self.glGetShaderiv = self._bind("glGetShaderiv", None, [c_uint, c_uint, POINTER(c_int)])
        self.glGetShaderInfoLog = self._bind("glGetShaderInfoLog", None, [c_uint, c_int, POINTER(c_int), POINTER(c_char)])
        self.glCreateProgram = self._bind("glCreateProgram", c_uint, [])
        self.glAttachShader = self._bind("glAttachShader", None, [c_uint, c_uint])
        self.glLinkProgram = self._bind("glLinkProgram", None, [c_uint])
        self.glGetProgramiv = self._bind("glGetProgramiv", None, [c_uint, c_uint, POINTER(c_int)])
        self.glGetProgramInfoLog = self._bind("glGetProgramInfoLog", None, [c_uint, c_int, POINTER(c_int), POINTER(c_char)])
        self.glUseProgram = self._bind("glUseProgram", None, [c_uint])

        # Buffers
        self.glGenBuffers = self._bind("glGenBuffers", None, [c_int, POINTER(c_uint)])
        self.glBindBuffer = self._bind("glBindBuffer", None, [c_uint, c_uint])
        self.glBufferData = self._bind("glBufferData", None, [c_uint, c_size_t, c_void_p, c_uint])

        # Textures
        self.glGenTextures = self._bind("glGenTextures", None, [c_int, POINTER(c_uint)])
        self.glBindTexture = self._bind("glBindTexture", None, [c_uint, c_uint])
        self.glTexImage2D = self._bind("glTexImage2D", None, [
            c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p
        ])

        # Framebuffers
        self.glGenFramebuffers = self._bind("glGenFramebuffers", None, [c_int, POINTER(c_uint)])
        self.glBindFramebuffer = self._bind("glBindFramebuffer", None, [c_uint, c_uint])

        # Uniforms
        self.glGetUniformLocation = self._bind("glGetUniformLocation", c_int, [c_uint, c_char_p])
        self.glUniformMatrix4fv = self._bind("glUniformMatrix4fv", None, [c_int, c_int, c_uint, POINTER(c_float)])

        # Viewport + Errors
        self.glViewport = self._bind("glViewport", None, [c_int, c_int, c_int, c_int])
        self.glGetError = self._bind("glGetError", c_uint, [])

        # Color
        self.glClearColor = self._bind("glClearColor", None, [c_float, c_float, c_float, c_float])
        self.glClear = self._bind("glClear", None, [c_uint])

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

        self.lib = None
        self.libGL = GLFunctions(self)
        if self.platform == "windows":
            from ctypes import wintypes as win
            self.win32 = win

        if libGL is not None:
            self.lib = cdll.LoadLibrary(libGL)
            self.lib_path = libGL
        else:
            if self.platform == "linux":
                self.lib = cdll.LoadLibrary("libGL.so.1")
                self.lib_path = "libGL.so.1"
            elif self.platform == "freebsd":
                self.lib = cdll.LoadLibrary("libGL.so")
                self.lib_path = "libGL.so"
                self.platform = "linux"
            elif self.platform == "openbsd":
                self.lib = cdll.LoadLibrary("libGL.so")
                self.lib_path = "libGL.so"
                self.platform = "linux"
            elif self.platform == "netbsd":
                self.lib = cdll.LoadLibrary("libGL.so")
                self.lib_path = "libGL.so"
                self.platform = "linux"
            elif self.platform == "windows":
                self.lib = ctypes.windll.opengl32
                self.lib_path = "opengl32.dll"
            elif self.platform == "darwin":
                self.lib = cdll.LoadLibrary("/System/Library/Frameworks/OpenGL.framework/OpenGL")
                self.lib_path = "/System/Library/Frameworks/OpenGL.framework/OpenGL"
            else:
                raise UnsupportedPlatform(f"Unsupported OS for GLX/OpenGL: {self.platform}, try passing lib path manually?")
        self.screen = screen

    def init(self, display: Any, window: Any, create_and_attach_ctx: bool=False):
        self._load_gl_functions()
        if self.platform == "linux":
            self.display = display
            self.window = window

            if create_and_attach_ctx:
                return self.create_context(display, window)
                
        elif self.platform == "windows":
            if not window:
                raise Exception("Provided Window's HWND is invalid, are you trying to draw on desktop? if yes, override this function!")

            self.window = window # display is useless

            self.gdi32 = ctypes.windll.gdi32
            self.user32 = ctypes.windll.user32

            if create_and_attach_ctx:
                return self.create_context(display, window)

    def clear(self, r: int, g: int, b: int, a: int):
        r = r / 255.0
        g = g / 255.0
        b = b / 255.0
        a = a / 255.0
        self.libGL.glClearColor(r, g, b, a)
        self.check_gl_error("glClearColor")
        self.libGL.glClear(GL_COLOR_BUFFER_BIT)
        self.check_gl_error("glClear")
    
    def swap(self):
        if self.platform == "linux":
            self.lib.glXSwapBuffers(self.display, self.window)
        elif self.platform == "windows":
            self.gdi32.SwapBuffers(self.hdc)

    def shutdown(self):
        self.destroy_context()

    def load_function(self, name: str, restype=None, argtypes: list=[]) -> c_void_p:
        addr = None
        if self.platform == "linux":
            addr = cast(self.lib.glXGetProcAddress(name.encode()), c_void_p)
        elif self.platform == "windows":
            addr = ctypes.cast(self.lib.wglGetProcAddress(name.encode()), ctypes.c_void_p)
            if not addr:
                try:
                    addr = getattr(self.lib, name)
                except AttributeError:
                    addr = None
        
            if not isinstance(addr, c_void_p): # it is a CFUNCTYPE
                addr = c_void_p(ctypes.cast(addr, c_void_p).value)

        if not addr:
            raise RuntimeError(f"Function {name} not found in GL driver")
        
        if isinstance(addr, c_void_p):
            addr = cast(addr, FuncType(restype, *argtypes))
        
        return addr
    
    def destroy_context(self):
        if self.ctx:
            if self.platform == "linux":
                self.lib.glXDestroyContext(self.display, self.ctx)
            elif self.platform == "windows":
                if self.ctx:
                    self.lib.wglDeleteContext(self.ctx)
                    self.ctx = None
                if self.hdc:
                    self.user32.ReleaseDC(self.ctx, self.hdc)
                    self.hdc = None
    
    def create_context(self, display, window):
        if self.platform == "linux":
            if self.ctx:
                self.destroy_context()

            attribs = (c_int * 5)(0x8010, 1, 0x8011, 1, 0)
            visual = self.lib.glXChooseVisual(display, 0, attribs)
            self.ctx = self.lib.glXCreateContext(display, visual, None, True)

            if not self.ctx:
                raise RuntimeError("Failed to create GLX Context")
            
            self.libGL._load_gl_functions_common()

            self.lib.glXMakeCurrent(display, window, self.ctx)

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
            self.user32.ShowWindow(window, 1)
            self.user32.UpdateWindow(window)
            self.user32.SetForegroundWindow(window)
            self.user32.BringWindowToTop(window)
            self.user32.RedrawWindow(window, None, None, 0x0001 | 0x0004 | 0x0080)  # RDW_INVALIDATE|UPDATENOW|FRAME

            # Sleep a tick to let composition settle (important on Windows 10/11 + Intel)
            import time
            time.sleep(0.1)

            self.hdc = self.user32.GetDC(window)
            
            if not self.hdc:
                raise RuntimeError(f"GetDC failed — invalid window handle: {window}")

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
            pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER
            pfd.iPixelType = PFD_TYPE_RGBA
            pfd.cColorBits = 32
            pfd.cDepthBits = 24
            pfd.cStencilBits = 8
            pfd.iLayerType = PFD_MAIN_PLANE

            exisiting_fmt = self.gdi32.GetPixelFormat(self.hdc)
            fmt = exisiting_fmt

            if exisiting_fmt == 0:
                fmt = self.gdi32.ChoosePixelFormat(self.hdc, ctypes.byref(pfd))
                if fmt == 0 or not self.gdi32.DescribePixelFormat(self.hdc, fmt, ctypes.sizeof(pfd), ctypes.byref(pfd)):
                    raise RuntimeError(f"ChoosePixelFormat failed - invalid HWND or HDC\n\tERR: {ctypes.GetLastError()}")
                if not self.gdi32.SetPixelFormat(self.hdc, fmt, ctypes.byref(pfd)):
                    raise RuntimeError(f"SetPixelFormat failed - could not set pixel format\n\tERR: {ctypes.GetLastError()}")

            # Create OpenGL rendering context
            self.ctx = self.lib.wglCreateContext(self.hdc)
            if not self.ctx:
                raise RuntimeError(f"Failed to create WGL Context\n\tERR: {ctypes.GetLastError()}")
            res = self.lib.wglMakeCurrent(self.hdc, self.ctx)
            if not res:
                raise RuntimeError(f"Failed to make WGL context current\n\tERR: {ctypes.GetLastError()}")


            current_ctx = self.lib.wglGetCurrentContext()
            if current_ctx != self.ctx:
                raise RuntimeError("WGL context is not current!")
            self.libGL._load_gl_functions_common()

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

    def check_gl_error(self, func: str="Unknown"):
        error = self.libGL.glGetError()
        if error != 0:
            print(f"OpenGL function [{func}] exited with an Error: {error}")

    def check_error(self):
        return self.check_gl_error("<UNSPECIFIED by USER>")

    def viewport(self, w: int=800, h: int=600):
        self.libGL.glViewport(0, 0, w, h)
        self.check_gl_error("glViewport")

    def create_shader(self, shader_type: int, source: str) -> int:
        shader = self.libGL.glCreateShader(shader_type)
        self.check_gl_error("glCreateShader")
        src = c_char_p(source.encode())
        length = c_int(len(source))
        self.libGL.glShaderSource(shader, 1, byref(src), byref(length))
        self.check_gl_error("glShaderSource")
        self.libGL.glCompileShader(shader)
        self.check_gl_error("glCompileShader")

        compiled = c_int()
        self.libGL.glGetShaderiv(shader, GL_COMPILE_STATUS, byref(compiled))
        self.check_gl_error("glGetShaderiv")
        if not compiled.value:
            log_len = c_int()
            self.libGL.glGetShaderiv(shader, GL_INFO_LOG_LENGTH, byref(log_len))
            self.check_gl_error("glGetShaderiv")
            log = create_string_buffer(log_len.value)
            self.libGL.glGetShaderInfoLog(shader, log_len, None, log)
            self.check_gl_error("glGetShaderInfoLog")
            raise RuntimeError(f"Shader Compile Error: {log.value.decode()}")
        return shader
    
    def create_program(self, vertex_shader: int, fragment_shader: int) -> int:
        program = self.libGL.glCreateProgram()
        self.check_gl_error("glCreateProgram")
        self.libGL.glAttachShader(program, vertex_shader)
        self.check_gl_error("glAttachShader")
        self.libGL.glAttachShader(program, fragment_shader)
        self.check_gl_error("glAttachShader")
        self.libGL.glLinkProgram(program)
        self.check_gl_error("glLinkProgram")

        linked = c_int()
        self.libGL.glGetProgramiv(program, GL_LINK_STATUS, byref(linked))
        self.check_gl_error("glGetProgramiv")
        if not linked.value:
            log_len = c_int()
            self.libGL.glGetProgramiv(program, 0x8B84, byref(log_len))
            self.check_gl_error("glGetProgramiv")
            log = create_string_buffer(log_len.value)
            self.libGL.glGetProgramInfoLog(program, log_len, None, log)
            self.check_gl_error("glGetProgramInfoLog")
            raise RuntimeError(f"Program link error: {log.value.decode()}")
        return program
    
    def use_program(self, program: int):
        self.libGL.glUseProgram(program)
        self.check_gl_error("glUseProgram")

    def create_buffer(self) -> int:
        buf = c_uint()
        self.libGL.glGenBuffers(1, byref(buf))
        self.check_gl_error("glGenBuffers")
        return buf.value
    
    def bind_array_buffer(self, buf: int):
        self.libGL.glBindBuffer(GL_ARRAY_BUFFER, buf)
        self.check_gl_error("glBindBuffer")

    def buffer_data(self, data, usage: int=GL_STATIC_DRAW):
        arr_type = c_float * len(data)
        self.libGL.glBufferData(GL_ARRAY_BUFFER, sizeof(arr_type), arr_type(*data), usage)
        self.check_gl_error("glBufferData")

    def create_texture(self) -> int:
        tex = c_uint()
        self.libGL.glGenTextures(1, byref(tex))
        self.check_gl_error("glGenTextures")
        return tex.value
    
    def bind_texture(self, texture: int, target: int=GL_TEXTURE_2D):
        self.libGL.glBindTexture(target, texture)
        self.check_gl_error("glBindTexture")
    
    def tex_image_2d(self, width: int, height: int, data: Any=None, target: int=GL_TEXTURE_2D, internal_format: int=0x1908, format_: int=0x1908, type_: int=0x1401):
        self.libGL.glTexImage2D(target, 0, internal_format, width, height, 0, format_, type_, data)
        self.check_gl_error("glTexImage2D")

    def create_framebuffer(self) -> int:
        fbo = c_uint()
        self.libGL.glGenFramebuffers(1, byref(fbo))
        self.check_gl_error("glGenFramebuffers")
        return fbo.value
    
    def bind_framebuffer(self, fbo: int, target: int=GL_FRAMEBUFFER):
        self.libGL.glBindFramebuffer(target, fbo)
        self.check_gl_error("glBindFramebuffer")

    def set_uniform_mat4(self, program: int, name: str, mat):
        loc = self.libGL.glGetUniformLocation(program, name.encode())
        self.check_gl_error("glGetUniformLocation")
        self.libGL.glUniformMatrix4fv(loc, 1, 0, (c_float * 16)(*mat))
        self.check_gl_error("glUniformMatrix4fv")

    def _load_gl_functions(self):
        """Loads OpenGL Functions (platform-based, .e.g GLX for linux, WGL for Windows)"""
        if self.platform == "linux":
            self.lib.glXChooseVisual.argtypes = [c_void_p, c_int, POINTER(c_int)]
            self.lib.glXChooseVisual.restype = c_void_p
            self.lib.glXCreateContext.argtypes = [c_void_p, c_void_p, c_void_p, c_int]
            self.lib.glXCreateContext.restype = c_void_p
            self.lib.glXMakeCurrent.argtypes = [c_void_p, c_ulong, c_void_p]
            self.lib.glXMakeCurrent.restype = c_int
            self.lib.glXSwapBuffers.argtypes = [c_void_p, c_uint64]
            self.lib.glXSwapBuffers.restype = c_void_p
            self.lib.glXDestroyContext.argtypes = [c_void_p, c_void_p]
            self.lib.glXDestroyContext.restype = c_void_p
            self.lib.glXGetProcAddress.argtypes = [c_char_p]
            self.lib.glXGetProcAddress.restype = c_void_p

        elif self.platform == "windows":
            self.lib.wglCreateContext.argtypes = [c_void_p]
            self.lib.wglCreateContext.restype = c_void_p
            self.lib.wglMakeCurrent.argtypes = [c_void_p, c_void_p]
            self.lib.wglMakeCurrent.restype = c_int
            self.lib.wglDeleteContext.argtypes = [c_void_p]
            self.lib.wglDeleteContext.restype = c_int
            self.lib.wglGetCurrentContext.argtypes = []
            self.lib.wglGetCurrentContext.restype = c_void_p
