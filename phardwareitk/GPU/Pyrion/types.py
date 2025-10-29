import sys
from typing import Any

class _PyrionBaseType(int):
    __slots__ = ()

    def __new__(cls, value, mask=0xFFFFFFFF):
        # Mask
        value = int(value) & mask
        return super().__new__(cls, value)

    def __add__(self, other):
        return _PyrionBaseType(int(self) + int(other))

    def __sub__(self, other):
        return _PyrionBaseType(int(self) - int(other))

    def __mul__(self, other):
        return _PyrionBaseType(int(self) * int(other))

    def __and__(self, other):
        return _PyrionBaseType(int(self) & int(other))

    def __or__(self, other):
        return _PyrionBaseType(int(self) | int(other))

    def __xor__(self, other):
        return _PyrionBaseType(int(self) ^ int(other))

    def __invert__(self):
        return _PyrionBaseType(~int(self))

class pyrion_uint64(_PyrionBaseType):
    """Represents unsigned integer of size 64-bits"""
    def __new__(cls, value):
        return super().__new__(cls, value, 0xFFFFFFFFFFFFFFFF)

    def __repr__(self):
        return f"pyrion_uint64({int(self)})"

class pyrion_uint32(_PyrionBaseType):
    """Represents unsigned integer of size 32-bits"""
    def __new__(cls, value):
        return super().__new__(cls, value, 0xFFFFFFFF)

    def __repr__(self):
        return f"pyrion_uint32({int(self)})"
    
class pyrion_uint16(_PyrionBaseType):
    """Represents unsigned integer of size 16-bits"""
    def __new__(cls, value):
        return super().__new__(cls, value, 0xFFFF)

    def __repr__(self):
        return f"pyrion_uint16({int(self)})"
    
class pyrion_uint8(_PyrionBaseType):
    """Represents unsigned integer of size 8-bits"""
    def __new__(cls, value):
        return super().__new__(cls, value, 0xFF)

    def __repr__(self):
        return f"pyrion_uint8({int(self)})"

class pyrion_int64(_PyrionBaseType):
    """Represents signed integer of size 64-bits"""
    def __new__(cls, value):
        value = int(value) & 0xFFFFFFFFFFFFFFFF
        # convert to signed range
        if value & 0x8000000000000000:
            value -= 0x10000000000000000
        return super().__new__(cls, value, 0xFFFFFFFFFFFFFFFF)

    def __repr__(self):
        return f"pyrion_int64({int(self)})"

class pyrion_int32(_PyrionBaseType):
    """Represents signed integer of size 32-bits"""
    def __new__(cls, value):
        value = int(value) & 0xFFFFFFFF
        if value & 0x80000000:
            value -= 0x100000000
        return super().__new__(cls, value, 0xFFFFFFFF)

    def __repr__(self):
        return f"pyrion_int32({int(self)})"
    
class pyrion_int16(_PyrionBaseType):
    """Represents signed integer of size 16-bits"""
    def __new__(cls, value):
        value = int(value) & 0xFFFF
        if value & 0x8000:
            value -= 0x10000
        return super().__new__(cls, value, 0xFFFF)

    def __repr__(self):
        return f"pyrion_int16({int(self)})"
    
class pyrion_int8(_PyrionBaseType):
    """Represents signed integer of size 8-bits"""
    def __new__(cls, value):
        value = int(value) & 0xFF
        if value & 0x80:
            value -= 0x100
        return super().__new__(cls, value, 0xFF)

    def __repr__(self):
        return f"pyrion_int8({int(self)})"

if sys.maxsize == 2**32:
    _BITS = 64
else:
    _BITS = 32

class pyrion_void:
    """Represents nothing, just an empty void"""
    __slots__ = ()

    def __repr__(self):
        return "pyrion_void()"
    
class _PyrionPointer:
    """Base class for Pyrion pointers."""
    __slots__ = ('address',)

    def __init__(self, address: int = 0):
        self.address = pyrion_uint64(address) if _BITS == 64 else pyrion_uint32(address)
        
    def __add__(self, other):
        return _PyrionPointer(int(self.address) + int(other))

    def __sub__(self, other):
        return _PyrionPointer(int(self.address) - int(other))

    def __repr__(self):
        return f"{self.__class__.__name__}({hex(self.address)})"

    def is_null(self):
        return self.address == 0
    
    def __eq__(self, other):
        return isinstance(other, _PyrionPointer) and self.__address == other.__address

    @classmethod
    def __class_getitem__(cls, *args):
        return cls

class pyrion_ptr(_PyrionPointer):
    """Generic typed pointer."""
    __slots__ = ('ptype', "_value")

    def __init__(self, ptype, value: Any=None):
        super().__init__(id(value))
        self.ptype = ptype  # what type this pointer points to
        self._value = value

    def cast(self, new_type):
        """Return a new pointer of different type."""
        return pyrion_ptr(new_type, self.address)

    def __repr__(self):
        return f"pyrion_ptr<{self.ptype.__name__}>({hex(self.address)})"
    
    @property
    def value(self) -> Any:
        return self._value
       
    def check_if_same(self, other):
        """Checks if the VALUE stored on both pointers are same"""
        return isinstance(other, pyrion_ptr) and self.value == other.value

class pyrion_structure_meta(type):
    """Meta for pyrion_structure to handle fields."""
    def __new__(cls, name, bases, namespace):
        fields = namespace.get("_struct_", [])
        size = 0
        offsets = {}

        # Compute offsets & total size
        for field in fields:
            if len(field) == 2:
                fname, ftype = field
                fsize = getattr(ftype, "_size_", 4)
            elif len(field) == 3:  # array
                fname, ftype, flen = field
                fsize = getattr(ftype, "_size_", 4) * flen
            else:
                raise ValueError("Invalid field tuple")
            offsets[fname] = size
            size += fsize

        namespace["_size_"] = size
        namespace["_offsets_"] = offsets
        return super().__new__(cls, name, bases, namespace)

class pyrion_structure(metaclass=pyrion_structure_meta): # Works like ctypes.Structure, so credits!
    _struct_ = []

    def __init__(self, mem: bytearray = None, offset: int = 0):
        self._mem = mem if mem is not None else bytearray(self._size_)
        self._offset = offset

    def __getattr__(self, name):
        if name in self._offsets_:
            offset = self._offsets_[name] + self._offset
            ftype = dict(self._struct_)[name]
            fsize = getattr(ftype, "_size_", 4)
            val_bytes = self._mem[offset:offset+fsize]
            # convert bytes to int for basic types
            if issubclass(ftype, _PyrionBaseType):
                return ftype(int.from_bytes(val_bytes, "little"))
            return val_bytes
        raise AttributeError(f"{name} not found")

    def __setattr__(self, name, value):
        if name in ("_mem", "_offset", "_struct_", "_size_", "_offsets_"):
            super().__setattr__(name, value)
        elif name in self._offsets_:
            offset = self._offsets_[name] + self._offset
            ftype = dict(self._struct_)[name]
            fsize = getattr(ftype, "_size_", 4)
            if issubclass(ftype, _PyrionBaseType):
                self._mem[offset:offset+fsize] = int(value).to_bytes(fsize, "little")
            else:
                # raw bytes assignment
                self._mem[offset:offset+fsize] = bytes(value)
        else:
            raise AttributeError(f"{name} not found")
