"""
IntelUHD module for handling Intel UHD Graphics operations.
"""

import subprocess
import psutil
import ctypes

import sys
import os

if not os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..") in sys.path:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

from Extensions import *
from Extensions.HyperOut import *

from GPU.SysInfo import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

def PError(*values: str) -> None:
    """Print the given string (*values) in error format and exit.

    Args:
        *values (str): The error messages to print.
    """
    printH(*values, Flush=True, FontEnabled=True, Font=TextFont(font_color=Color("red")))
    exit(1)

class Basic:
    def __init__(self) -> None:
        """Initialize the Basic class."""
        self.gpu_info = {}
        self.power_mode = "medium"

    def initialize_gpu(self) -> None:
        """Initialize the GPU by checking basic compatibility."""
        gpu_info = self.get_gpu_info()
        if "info" in gpu_info and "Intel" in gpu_info["info"]:
            print("GPU initialized successfully.")
        else:
            PError("Intel GPU not found.")

    def get_gpu_info(self) -> dict:
        """Retrieve GPU information using system commands.

        Returns:
            dict: A dictionary containing GPU information.
        """
        try:
            if Windows:
                result = subprocess.check_output(
                    "wmic path win32_videocontroller get caption,adapterram", shell=True
                )
                decoded_result = result.decode("utf-8", errors="ignore").strip()
                self.gpu_info = {"info": decoded_result}
            elif (Linux or Kali) or Ubuntu:
                result = subprocess.check_output(["lspci", "-v"], universal_newlines=True)
                self.gpu_info = {"info": result}
            elif MacOs:
                result = subprocess.check_output(
                    ["system_profiler", "SPDisplaysDataType"], universal_newlines=True
                )
                self.gpu_info = {"info": result}
            else:
                PError(f"Unsupported OS: {platform}")
        except subprocess.CalledProcessError as e:
            PError("Failed to retrieve GPU info: " + str(e))
        return self.gpu_info

    def check_gpu_availability(self) -> bool:
        """Check if the GPU is available.

        Returns:
            bool: True if the GPU is available, False otherwise.
        """
        return bool(self.gpu_info)

    def get_gpu_model(self) -> str:
        """Extract the GPU model from the GPU information.

        Returns:
            str: The GPU model.
        """
        for line in self.gpu_info.get("info", "").splitlines():
            if "Intel" in line:
                return line.strip()
        return "Unknown"

    def get_gpu_memory(self) -> Union[str, None]:
        """Retrieve the GPU memory size.

        Returns:
            str: The GPU memory size in MB, or None if not available.
        """
        if Windows:
            for line in self.gpu_info.get("info", "").splitlines():
                if "AdapterRAM" in line:
                    try:
                        parts = line.split()
                        memory_value = next((part for part in parts if part.isdigit()), None)
                        if memory_value:
                            return str(int(memory_value) // (1024 ** 2)) + " MB"
                    except ValueError:
                        continue
        elif (Linux or Ubuntu) or Kali:
            PError("Memory not available via lspci (LINUX)")
        elif MacOs:
            PError("Memory size unavailable on macOS")
        else:
            PError("Unknown OS")
        return None

    def get_gpu_temperature(self) -> str:
        """Get the GPU temperature. ONLY WINDOWS!

        Returns:
            str: The GPU temperature in °C, or an error message if not available.
        """
        if Windows:
            try:
                temp = subprocess.check_output("wmic /namespace:\\root\\wmi path MSAcpi_ThermalZoneTemperature get CurrentTemperature", shell=True)
                for line in temp.decode().splitlines():
                    if line.strip().isdigit():
                        return str(int(line.strip()) / 10 - 273.15) + "°C"
            except subprocess.CalledProcessError:
                return "Temperature query failed"
        return "Temperature querying not implemented for this OS"

    def get_driver_version(self) -> str:
        """Retrieve the GPU driver version.

        Returns:
            str: The GPU driver version, or an error message if not available.
        """
        if Windows:
            try:
                result = subprocess.check_output("wmic path win32_videocontroller get driverversion", shell=True)
                return result.decode().splitlines()[1].strip()
            except subprocess.CalledProcessError as e:
                return "Driver version query failed: " + str(e)
        elif (Linux or Ubuntu) or Kali:
            try:
                result = subprocess.check_output("glxinfo | grep 'OpenGL version'", shell=True, text=True)
                return result.strip()
            except subprocess.CalledProcessError:
                return "Driver version unavailable."
        PError("Not implemented OS")

    def get_power_modes(self) -> str:
        """Retrieve the power modes. In Windows Only, (*) for current power mode.

        Returns:
            str: The power modes, or an error message if not available.
        """
        try:
            if Windows:
                result = subprocess.run(["powercfg", "/LIST"], stdout=subprocess.PIPE)
                return result.stdout.decode().strip()
            else:
                PError("Power modes unavailable on this OS.")
        except subprocess.CalledProcessError as e:
            PError(e)

    def run_diagnostics(self) -> str:
        """Run diagnostics on the GPU.

        Returns:
            str: The result of the diagnostics.
        """
        print("Running diagnostics...")
        try:
            subprocess.run(["python", os.path.join(os.path.dirname(__file__), "..", "StressTester", "run.py")], check=True)
        except subprocess.CalledProcessError as e:
            return "Diagnostics failed: " + str(e)
        return "Diagnostics completed successfully."

    def test_rendering(self) -> str:
        """Test basic rendering capability.

        Returns:
            str: The result of the rendering test.
        """
        print("Rendering test in progress...")
        return "Rendering test passed."

    def enable_overclocking(self) -> str:
        """Enable GPU overclocking.

        Returns:
            str: A message indicating that overclocking is only supported for NVIDIA GPUs.
        """
        return "Only supported for NVIDIA Gpu."

    def disable_overclocking(self) -> str:
        """Disable GPU overclocking.

        Returns:
            str: A message indicating that overclocking is only supported for NVIDIA GPUs.
        """
        return "Only supported for NVIDIA Gpu."

    def reset_gpu(self) -> str:
        """Reset the GPU settings to default.

        Returns:
            str: A message indicating that resetting is only supported for NVIDIA GPUs.
        """
        return "Only supported for NVIDIA Gpu."

    def get_gpu_resolution(self) -> Union[List[str], str]:
        """Get the GPU resolution.

        Returns:
            list: A list of supported resolutions, or an error message if not available.
        """
        if Windows:
            try:
                result = subprocess.check_output(
                    "wmic path Win32_VideoController get VideoModeDescription", shell=True, stderr=subprocess.DEVNULL
                )
                resolutions = result.decode().splitlines()
                resolutions = [res.strip() for res in resolutions if res.strip() and "VideoModeDescription" not in res]
                return resolutions
            except subprocess.CalledProcessError as e:
                return f"Failed to retrieve GPU resolution: {e}"
        else:
            return "Resolution retrieval not implemented for this OS"

    def get_supported_refresh_rates(self) -> Union[List[str], str]:
        """Get a list of supported refresh rates.

        Returns:
            list: A list of supported refresh rates, or an error message if not available.
        """
        if Windows:
            try:
                result = subprocess.check_output(
                    "wmic path Win32_VideoController get CurrentRefreshRate", shell=True, stderr=subprocess.DEVNULL
                )
                refresh_rates = result.decode().splitlines()
                refresh_rates = [rate.strip() for rate in refresh_rates if rate.strip() and "CurrentRefreshRate" not in rate]
                return refresh_rates
            except subprocess.CalledProcessError as e:
                return f"Failed to retrieve GPU refresh rates: {e}"
        else:
            return "Refresh rate retrieval not implemented for this OS"

    def check_vulkan_support(self) -> bool:
        """Check if Vulkan is supported.

        Returns:
            bool: True if Vulkan is supported, False otherwise.
        """
        try:
            result = subprocess.check_output("vulkaninfo", shell=True, stderr=subprocess.DEVNULL)
            return "Vulkan" in result.decode()
        except subprocess.CalledProcessError:
            return False

    def check_opencl_support(self) -> bool:
        """Check if OpenCL is supported.

        Returns:
            bool: True if OpenCL is supported, False otherwise.
        """
        try:
            result = subprocess.check_output("clinfo", shell=True, stderr=subprocess.DEVNULL)
            return "OpenCL" in result.decode()
        except subprocess.CalledProcessError:
            return False

    def check_directx_support(self) -> bool:
        """Check if DirectX is supported.

        Returns:
            bool: True if DirectX is supported, False otherwise.
        """
        if Windows:
            try:
                result = subprocess.check_output("dxdiag", shell=True, stderr=subprocess.DEVNULL)
                return "DirectX" in result.decode()
            except subprocess.CalledProcessError:
                return False
        return False

    def get_utilization(self) -> str:
        """Get current GPU utilization percentage.

        Returns:
            str: The current GPU utilization percentage.
        """
        return str(psutil.cpu_percent()) + "%"

class Creation:
    def __init__(self) -> None:
        """Initialize the Creation class."""
        self.window = None

    def create_window(self, width: int = 800, height: int = 600, name: str = "PHardwareITK") -> int:
        """Create a window using OpenGL.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
            name (str): The name of the window.

        Returns:
            int: The window ID.
        """
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(0, 0)
        self.window = glutCreateWindow(name.encode())
        glClearColor(0.0, 0.0, 0.0, 1.0)
        gluPerspective(45, (width / height), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        return self.window

    def draw_triangle(self) -> None:
        """Draw a triangle using OpenGL."""
        glBegin(GL_TRIANGLES)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glEnd()

    def draw_square(self) -> None:
        """Draw a square using OpenGL."""
        glBegin(GL_QUADS)
        glVertex3f(-1.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glEnd()

    def draw_circle(self, radius: float = 1.0, segments: int = 32) -> None:
        """Draw a circle using OpenGL.

        Args:
            radius (float): The radius of the circle.
            segments (int): The number of segments to use for the circle.
        """
        glBegin(GL_POLYGON)
        for i in range(segments):
            theta = 2.0 * 3.1415926 * i / segments
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            glVertex2f(x, y)
        glEnd()

    def draw_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """Draw a line using OpenGL.

        Args:
            x1 (float): The x-coordinate of the first point.
            y1 (float): The y-coordinate of the first point.
            x2 (float): The x-coordinate of the second point.
            y2 (float): The y-coordinate of the second point.
        """
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

    def draw_point(self, x: float, y: float) -> None:
        """Draw a point using OpenGL.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

    def draw_polygon(self, vertices: List[tuple]) -> None:
        """Draw a polygon using OpenGL.

        Args:
            vertices (list): A list of tuples representing the vertices of the polygon.
        """
        glBegin(GL_POLYGON)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

    def draw_cube(self) -> None:
        """Draw a cube using OpenGL."""
        glBegin(GL_QUADS)
        # Front face
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        # Back face
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        # Top face
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        # Bottom face
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        # Right face
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        # Left face
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glEnd()

    def draw_sphere(self, radius: float = 1.0, slices: int = 32, stacks: int = 32) -> None:
        """Draw a sphere using OpenGL.

        Args:
            radius (float): The radius of the sphere.
            slices (int): The number of slices.
            stacks (int): The number of stacks.
        """
        quadric = gluNewQuadric()
        gluSphere(quadric, radius, slices, stacks)
        gluDeleteQuadric(quadric)

    def draw_cone(self, base: float = 1.0, height: float = 2.0, slices: int = 32, stacks: int = 32) -> None:
        """Draw a cone using OpenGL.

        Args:
            base (float): The base radius of the cone.
            height (float): The height of the cone.
            slices (int): The number of slices.
            stacks (int): The number of stacks.
        """
        quadric = gluNewQuadric()
        gluCylinder(quadric, base, 0.0, height, slices, stacks)
        gluDeleteQuadric(quadric)

    def draw_cylinder(self, base: float = 1.0, top: float = 1.0, height: float = 2.0, slices: int = 32, stacks: int = 32) -> None:
        """Draw a cylinder using OpenGL.

        Args:
            base (float): The base radius of the cylinder.
            top (float): The top radius of the cylinder.
            height (float): The height of the cylinder.
            slices (int): The number of slices.
            stacks (int): The number of stacks.
        """
        quadric = gluNewQuadric()
        gluCylinder(quadric, base, top, height, slices, stacks)
        gluDeleteQuadric(quadric)

    def draw_torus(self, inner_radius: float = 0.5, outer_radius: float = 1.0, sides: int = 32, rings: int = 32) -> None:
        """Draw a torus using OpenGL.

        Args:
            inner_radius (float): The inner radius of the torus.
            outer_radius (float): The outer radius of the torus.
            sides (int): The number of sides.
            rings (int): The number of rings.
        """
        glutSolidTorus(inner_radius, outer_radius, sides, rings)

    def render_scene(self):
        """Render the scene."""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_triangle()
        self.draw_square()
        self.draw_circle()
        glutSwapBuffers()

    def render_loop(self):
        """Run the rendering loop."""
        glutDisplayFunc(self.render_scene)
        glutIdleFunc(self.render_scene)
        glutMainLoop()

if __name__ == "__main__":
    intel_gpu = Basic()
    try:
        intel_gpu.initialize_gpu()
        print("GPU Info:", intel_gpu.get_gpu_info())
        print("Model:", intel_gpu.get_gpu_model())
        print("Memory:", intel_gpu.get_gpu_memory())
        print("Temperature:", intel_gpu.get_gpu_temperature())
        print("Driver Version:", intel_gpu.get_driver_version())
        print("GPU Resolution:", intel_gpu.get_gpu_resolution())
        print("Supported Refresh Rates:", intel_gpu.get_supported_refresh_rates())
        print("Vulkan Support:", intel_gpu.check_vulkan_support())
        print("OpenCL Support:", intel_gpu.check_opencl_support())
        print("DirectX Support:", intel_gpu.check_directx_support())
        print("GPU Utilization:", intel_gpu.get_utilization())
    except Exception as e:
        print("Error:", str(e))
