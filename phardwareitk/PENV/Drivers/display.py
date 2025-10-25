# NEVER GIVE UP!!!
import os
import sys
import platform

module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
if not module_path in sys.path:
    sys.path.append(module_path)

if platform.system().lower() == "windows":
    from ctypes import wintypes
    import ctypes
    class WindowsFrameBufferDriver:
        def __init__(self, w, h, d, classn="Static", windown="Pheonix Virtual Environment"):
            from phardwareitk.GUI import gui_sdl as gui

            self.w:int = w
            self.h:int = h
            self.d:int = d

            self.pitch = (self.w * self.d + 3) & ~3
            self.vram = bytearray(self.pitch * self.h)

            self.classn = classn
            self.windown = windown

            self.deleted = False

            self.gui = gui

            self.gui.initialize()
            self.gui.InitializePError()
            self.gui.ExtensionsInit()
            self.window = self.gui.CreateWindow(windown, w, h, self.gui.SDL_WINDOWPOS_CENTERED, None, 0, 0)
            self.renderer = self.gui.MakeRenderer(self.window, -1, self.gui.SDL_RENDERER_ACCELERATED)

            self.gui.UpdateWindow(self.window)

            self.gui.TitleBarWindows(None, "dark")

            self.gui.UpdateWindow(self.window)

        def wp(self, x, y, r, g, b):
            if 0 <= x < self.w and 0 <= y < self.h:
                offset = (y * self.pitch + x) * self.d
                self.vram[offset:offset+3] = bytes([r, g, b])

        def cl(self, r, g, b):
            color = bytes([r, g, b])
            for y in range(self.h):
                for x in range(self.w):
                    offset = (y * self.pitch + x) * self.d
                    self.vram[offset:offset+3] = color

        def flush(self):
            vram_ptr = (ctypes.c_ubyte * len(self.vram)).from_buffer(self.vram)
            surface = self.gui.SDL_CreateRGBSurfaceFrom(vram_ptr, self.w, self.h, 24, self.pitch,
                                                   0x000000FF, 0x0000FF00, 0x00FF0000, 0)
            self.gui.SDL_BlitSurface(surface, None, self.gui.SDL_GetWindowSurface(self.window), None)
            self.gui.SDL_UpdateWindowSurface(self.window)

        def msg_loop(self):
            self.gui.EventLoop(True, self.window, None, None, self.renderer, True)
            self.__del__()

        def __del__(self):
            if not self.deleted:
                self.gui.DestroyWindow(self.window, None, None)
                self.gui.DeinitializePError()
                self.gui.Quit()
                self.deleted = True

else:
    import mmap
    class LinuxFrameBufferDriver:
        def __init__(self, w, h, d):
            self.w = w
            self.h = h
            self.d = d

            self.fb = os.open("/dev/fb0", os.O_RDWR)
            self.screensize = self.w * self.h * self.d

            self.vram = bytearray(self.screensize)
            self.mm = mmap.mmap(
                self.fb, self.screensize, mmap.MAP_SHARED, mmap.PROT_WRITE | mmap.PROT_READ
            )

        def wp(self, x, y, r, g, b):
            if x < 0 or (y < 0 or (x >= self.w or y >= self.h)):
                return

            offset = (y * self.w + x) * self.d
            self.vram[offset : offset + 3] = bytes([b, g, r])  # Linux has BGR framebuffer

        def cl(self, r, g, b):
            for y in range(self.h):
                for x in range(self.w):
                    self.wp(x, y, r, g, b)

        def flush(self):
            self.mm.seek(0)
            self.mm.write(self.vram)

        def __del__(self):
            self.mm.close()
            os.close(self.fb)
