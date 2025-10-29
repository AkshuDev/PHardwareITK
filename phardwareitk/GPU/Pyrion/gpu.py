"""Pyrion GPU"""
from typing import *

from .constants import *

_gpu_context = None

def base_pyrion_msg_handler(stream: PSTREAM, *args) -> Any:
    """Basic Pyrion Message Handler"""
    stream.value(*args)

def base_pyrion_err_stream(*args) -> None:
    """Default Pyrion Error stream"""
    from phardwareitk.Extensions.HyperOut import printH
    from phardwareitk.Extensions import Color, TextFont

    printH(*args, FontEnabled=True, Font=TextFont(font_color=Color("red"), Bold=True))

class PyrionGPU:
    """
    Represents the Virtual GPU. Handles memory, shaders, execution, and more...
    
    NOTE: Uses the CPU, for GPU usage, please resort to using PyrionGPU driver for AOS++, CPU is the only option because Operating Systems like Window do not give GPU access without going through layers like OpenGL/Vulkan/DirectX/etc which makes it more complex and can't be highly feature rich because it will in end have to rely on already made systems.
    """
    def __init__(self):
        self.initialized = False

        self.nextalloc = {
            "array": 0
        }

        self.memory = bytearray()
        self.framebuffer = bytearray()
        self.meminfo = {}
        self.shaders = {}
        self.kernels = {}
        self.context_info = self.detect_hardware()

        self.outstream = PSTREAM(object, print)
        self.instream = PSTREAM(object, input)
        self.errstream = PSTREAM(object, base_pyrion_err_stream)

        self.iohandler = base_pyrion_msg_handler

    def detect_hardware(self) -> Dict[str, Any]:
        """Detect the GPU capabilities and resources available"""
        return {
            "name": "Pyrion Virtual GPU",
            "vendor": "Pheonix Studios",
            "max_memory": 1024 * 1024 * 1024, # 1 GB
            "supported_shaders": ["vertex", "fragment", "compute"]
        }
    
    def print(self, *args) -> None:
        """Outputs the *args to the output stream"""
        self.iohandler(self.outstream, *args)

    def fprint(self, stream: PSTREAM, *args) -> None:
        """Outputs at specified stream"""
        stream.value(*args)

    def change_stream(self, stream: PSTREAM, stream_type: PSTREAMID) -> None:
        """Change the current <stream_type> to <stream>"""
        if stream_type == PSTREAMOUT:
            self.outstream = stream
        elif stream_type == PSTREAMIN:
            self.instream = stream
    
    def initialize(self, memory_size: PLONG) -> None:
        """Initialize the GPU with specified memory size"""
        if self.initialized: self.fprint(self.errstream, "Pyrion is already initialized!")
        self.print("Initializing Pyrion VGPU...")
        self.initialized = True
        self.memory = bytearray(int(memory_size))
        self.print("Pyrion VGPU is initialized!")

    def allocate_mem(self, value: PLONG, mem_type:PMEMID) -> PMEMORY:
        """Allocates Pyrion memory for a object, returns PMEMORY (*long)"""
        if mem_type == PMEM_ARRAY:
            ret = PMEMORY(id(self.memory) + self.nextalloc["array"])
            self.meminfo[ret.address] = {
                "type": int(mem_type),
                "size": int(value)
            }

            self.nextalloc["array"] += value
            self.print(f"Allocated memory of size {hex(value)}")
            return ret

    def free_mem(self, memory: PMEMORY) -> None:
        mem = self.meminfo.get(memory.address, None)
        if not mem:
            self.fprint(self.errstream, f"No such allocated memory at address {hex(memory.address)}")
            return None
        
        if mem["type"] == int(PMEM_ARRAY):
            self.write_mem(memory, pyrion_ptr(bytes, b"\x00"*mem["size"]), POFFSET(0))
        
    def write_mem(self, ptr: PMEMORY, data_ptr: PBYTES, offset: POFFSET=POFFSET(0)):
        """Write data into VRAM at pointer offset"""

        data = data_ptr.value

        start = ptr.address - id(self.memory) + offset
        end = start + len(data)
        self.memory[start:end] = data

    def read_mem(self, ptr: PMEMORY, size: PLONG, offset: POFFSET=POFFSET(0)) -> bytes:
        start = ptr.address - id(self.memory) + offset
        return self.memory[start:start+size]
    
    def create_ctx(self, ctx_info: PCTX_INFO) -> PCONTEXT:
        """Creates a context based on the context info, this context have to then be attached though"""
        ctx = PCONTEXT()
        ctx.handle = PHANDLE(0) # None
        ctx.pixel_size = ctx_info.pixel_size
        ctx.pixel_depth = ctx_info.pixel_depth
        ctx.fb_initialclr = ctx_info.initcolor
        ctx.fb_width = ctx_info.width
        ctx.fb_height = ctx_info.height

        return ctx
    
    