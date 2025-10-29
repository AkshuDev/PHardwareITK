import sys
import os

if not os.path.join(os.path.dirname(__file__), "..") in sys.path:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from phardwareitk.GPU.Pyrion import *
from phardwareitk.GPU.Pyrion.gpu import *

pyrion = PyrionGPU()

memsize = PLONG(1024*1024) # 1MB of memory

print("MEMORY SIZE: ", memsize)

pyrion.initialize(memsize) # Init
ptr = pyrion.allocate_mem(PLONG(12), PMEM_ARRAY) # Allocate 12 bytes

print("Allocated Pointer:", ptr)

pyrion.free_mem(ptr) # Free the memory