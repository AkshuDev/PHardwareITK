import sys

from .types import *
from .types import _PyrionPointer

if sys.maxsize > 2**32:
    PBITS = 64
else:
    PBITS = 32

# Typedefs
PBYTE = pyrion_int8
PSHORT = pyrion_int16
PINT = pyrion_int32
_PLONG = pyrion_int64 if PBITS == 64 else pyrion_int32 # Did this to fix typing issue
PLONG = _PLONG
PUBYTE = pyrion_uint8
PUSHORT = pyrion_uint16
PUINT = pyrion_uint32
_PULONG = pyrion_uint64 if PBITS == 64 else pyrion_uint32 # same reason
PULONG = _PULONG

PBYTES = pyrion_ptr[bytes]

PNULL = pyrion_void

PSTREAMID = PUINT
PYID = PUINT
PSHADERID = PUINT
PMEMID = PLONG

PSIZE = PUINT
PLEN = PUINT
POFFSET = PLONG

PVOID = pyrion_ptr[PNULL]
PSTREAM = pyrion_ptr[object]
PMEMORY = _PyrionPointer[PMEMID]
PBUFFER = pyrion_ptr[PULONG]

PSTREAMOUT = PSTREAMID(1)
PSTREAMIN = PSTREAMID(0)

PMEM_ARRAY = PMEMID(0)
PMEM_BUFF = PMEMID(1)
PMEM_VERTEX = PMEMID(2)

PIXEL_SIZE = PUINT
PIXEL_RGB = PIXEL_SIZE(3)
PIXEL_RGBA = PIXEL_SIZE(4)

PHANDLE = PLONG

class PCONTEXT(pyrion_structure):
    _struct_ = [
        ("handle", PHANDLE),
        ("pixel_size", PIXEL_SIZE),
        ("pixel_depth", PUBYTE),
        ("fb_initialclr", PUINT),
        ("fb_width", PUINT),
        ("fb_height", PUINT)
    ]

class PCTX_INFO(pyrion_structure):
    _struct_ = [
        ("ctx", PCONTEXT),
        ("pixel_size", PIXEL_SIZE),
        ("pixel_depth", PUBYTE),
        ("width", PUINT),
        ("height", PUINT),
        ("initcolor", PUINT),
    ]