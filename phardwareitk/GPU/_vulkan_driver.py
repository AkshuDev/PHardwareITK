"""Vulkan Driver implementation using BaseGPUD class (incomplete)"""

import ctypes
import platform
from typing import Any
from phardwareitk.GPU._base import BaseGPUD

VK_SUCCESS = 0
VK_STRUCTURE_TYPE_APPLICATION_INFO = 0
VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO = 1
VK_API_VERSION_1_0 = (1 << 22) | (0 << 12) | 0 # Vulkan 1.0

class VulkanDriver(BaseGPUD):
    def __init__(self):
        self.platform = platform.system().lower()

        self.lib = None

        if self.platform == "windows":
            self.lib = ctypes.WinDLL("vulkan-1.dll")
        else:
            self.lib = ctypes.CDLL('libvulkan.so.1')

        self.instance = None
        self.physical_device = None
        self.device = None
        self.queue = None
        self.surface = None
        self.swapchain = None
        self.cmd_pool = None

    def init(self, display: Any, window: Any, create_and_attach_ctx = False):
        class VkApplicationInfo(ctypes.Structure):
            _fields_ = [
                ("sType", ctypes.c_int),
                ("pNext", ctypes.c_void_p),
                ("pApplicationName", ctypes.c_char_p),
                ("applicationVersion", ctypes.c_uint32),
                ("pEngineName", ctypes.c_char_p),
                ("engineVersion", ctypes.c_uint32),
                ("apiVersion", ctypes.c_uint32),
            ]

        app_info = VkApplicationInfo(
            sType=VK_STRUCTURE_TYPE_APPLICATION_INFO,
            pNext=None,
            pApplicationName=b"PheonixIon Vulkan",
            applicationVersion=1,
            pEngineName=b"PheonixIon Engine",
            engineVersion=1,
            apiVersion=VK_API_VERSION_1_0,
        )

        class VkInstanceCreateInfo(ctypes.Structure):
            _fields_ = [
                ("sType", ctypes.c_int),
                ("pNext", ctypes.c_void_p),
                ("flags", ctypes.c_uint32),
                ("pApplicationInfo", ctypes.POINTER(VkApplicationInfo)),
                ("enabledLayerCount", ctypes.c_uint32),
                ("ppEnabledLayerNames", ctypes.POINTER(ctypes.c_char_p)),
                ("enabledExtensionCount", ctypes.c_uint32),
                ("ppEnabledExtensionNames", ctypes.POINTER(ctypes.c_char_p)),
            ]

        create_info = VkInstanceCreateInfo(
            sType=VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
            pNext=None,
            flags=0,
            pApplicationInfo=ctypes.pointer(app_info),
            enabledLayerCount=0,
            ppEnabledLayerNames=None,
            enabledExtensionCount=0,
            ppEnabledExtensionNames=None,
        )

        vkCreateInstance = self.load_function("vkCreateInstance")
        vkCreateInstance.restype = ctypes.c_int
        vkCreateInstance.argtypes = [ctypes.POINTER(VkInstanceCreateInfo), ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)]

        instance = ctypes.c_void_p()
        result = vkCreateInstance(ctypes.byref(create_info), None, ctypes.byref(instance))
        if result != VK_SUCCESS:
            raise RuntimeError(f"Failed to create Vulkan instance: {result}")

        self.instance = instance

        if create_and_attach_ctx:
            self.create_context(display, window)

    def load_function(self, name: str):
        try:
            return getattr(self.lib, name)
        except AttributeError:
            return None
        
    def create_context(self, display: Any, window: Any):
        pass

    def shutdown(self):
        if self.instance:
            vkDestroyInstance = self.load_function("vkDestroyInstance")
            if vkDestroyInstance:
                vkDestroyInstance(self.instance, None)
            self.instance = None
