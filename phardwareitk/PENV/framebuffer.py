import os
import sys

module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

if not module_path in sys.path:
    sys.path.append(module_path)

from phardwareitk.PENV.shared import *

from phardwareitk.PENV.Drivers.display import *

# Never Give UP!!!!

class Framebuffer:
    """Bro i lost my mind building this"""

    def __init__(self, width: int, height: int, depth: int = 3, classNameWin32:str="Static", winNameWin32:str="Framebuffer") -> None:
        """Initialize the framebuffer with specified dimensions and depth."""
        self.width: int = width
        self.height: int = height
        self.depth: int = depth
        self.driver = None
        self.win32, self.posix, self.unknown, self.host_os = get_os()
        self.running = True  # Control flag for the message loop thread
        if self.posix:
            self.driver: LinuxFrameBufferDriver = LinuxFrameBufferDriver(width, height, depth)
        elif self.win32:
            self.driver: WindowsFrameBufferDriver = WindowsFrameBufferDriver(width, height, depth, classNameWin32, winNameWin32)

    def write_pixel(self, x=0, y=0, r=0, g=0, b=0) -> None:
        """Write a pixel to the framebuffer at the specified coordinates with the given RGB color."""
        return self.driver.wp(x, y, r, g, b)

    def clear(self, r=0, g=0, b=0) -> None:
        """Clear the framebuffer with the specified RGB color."""
        return self.driver.cl(r, g, b)

    def flush(self) -> None:
        """Flush the framebuffer to the display."""
        return self.driver.flush()

    def handle_events(self) -> None:
        """Handle events for the framebuffer driver."""
        if self.driver is not None:
            self.driver.msg_loop()

    def lserialize(self) -> list:
        """Serialize the framebuffer dimensions into a list."""
        return [self.width, self.height, self.depth]

    def delete(self) -> None:
        """Delete the framebuffer and clean up resources."""
        self.running = False  # Signal
        if self.driver is not None:
            del self.driver

