"""This is the new and improved C Extension, which allows for easy usage. It allows emulating C in python to do tasks that Cython/C Can do in python by emulating it."""

from typing import Union, Optional
from phardwareitk.Memory import Memory

memory: Memory = None
memsize: int = 64

heap_ptr: int = 0x0
heap_nextalloc: int = 0x0
heap_registry: dict[int, int] = {}

stack_ptr = memsize

def align(v1: int, v2: int) -> int:
    return ((v1 + v2 - 1) // v2) * v2

def reset_mem(new_size: int) -> None:
    """Resets the memory with new size, expanding or shrinking it"""
    global memory
    global memsize
    global stack_ptr
    memsize = new_size
    memory = Memory(new_size, system_size=0, proc_sector_size=0, Block=None)
    stack_ptr = new_size

def initialize(size: int=64) -> None:
    """Initializes the memory, very important to use this before using anything else!"""
    reset_mem(size)

def write_mem(data:bytes, size:int, addr:int) -> None:
    """Writes data of specified size at the specified address"""
    global memory
    global memsize

    if addr > memsize:
        raise OSError(
            f"Trying to access memory outside of the virtual memory space using address [{hex(addr)}], while virtual memory has a size of [{hex(memsize)}]. [ERROR:PHardwareITK:Extensions:C - set_mem]"
        )

    data_ = data[:size]
    if size == len(data): data_ = data

    memory.write_ram(data_, addr, 0)

def read_mem(size:int, addr: int) -> bytes:
    """Reads the specified size from the specified address from memory."""
    global memory
    global memsize

    if addr > memsize:
        raise OSError(
            f"Trying to access memory outside of the virtual memory space using address [{hex(addr)}], while virtual memory has a size of [{hex(memsize)}]. [ERROR:PHardwareITK:Extensions:C - set_mem]"
        )

    return memory.get_ram(size, addr)

def delete_mem(size: int, addr: int) -> None:
    """Deletes/Clears memory at specified address for specified size"""
    write_mem(b"\x00"*size, size, addr)

def stack_push(data: bytes) -> None:
    """Pushes data onto the stack"""
    global stack_ptr

    size = align(len(data), 8)
    if size > len(data):
        data.rjust(size, b"\x00")
    elif size < len(data):
        data = data[:size]

    write_mem(data, size, stack_ptr)
    stack_ptr -= size

def stack_pop(count: int) -> bytes:
    """Pops 8 bytes off the stack for specifed 'count' times and returns it concatinated"""
    global stack_ptr
    global memsize

    data: bytes = b""

    for i in range(0, count):
        stack_ptr += 8
        if stack_ptr > memsize: raise ValueError("Nothing to pop, Exceeding memory limits!")
        data += read_mem(8, stack_ptr)

    return data

class CBaseType():
    size = 1
    signed = True

    def __init__(self, value:int) -> None:
        if signed:
            if size == 1:
                if value < -0x80 or value > 0x7F:
                    raise ValueError("Value doesn't fit in 1 bytes!")
            elif size == 2:
                if value < -0x8000 or value > 0x7FFF:
                    raise ValueError("Value doesn't fit in 2 bytes!")
            elif size == 4:
                if value < -0x80000000 or value > 0x7FFFFFFF:
                    raise ValueError("Value doesn't fit in 4 bytes!")
            elif size == 8:
                if value < -0x8000000000000000 or value > 0x7FFFFFFFFFFFFFFF:
                    raise ValueError("Value doesn't fit in 8 bytes!")
            else:
                raise ValueError(f"Unknown size: {size} bytes")

        else:
            if value < 0:
                raise ValueError("Value is signed while it was supposed to be unsigned!")
            if size == 1:
                if value > 0xFF:
                    raise ValueError("Value doesn't fit in 1 byte!")
            elif size == 2:
                if value > 0xFFFF:
                    raise ValueError("Value doesn't fit in 2 bytes!")
            elif size == 4:
                if value > 0xFFFFFFFF:
                    raise ValueError("Value doesn't fit in 4 bytes!")
            elif size == 8:
                if value > 0xFFFFFFFFFFFFFFFF:
                    raise ValueError("Value doesn't fit in 8 bytes!")
            else:
                raise ValueError(f"Unknown size: {size} bytes")

        self.value = value
        self.address = stack_ptr
        stack_push(value.to_bytes(size, "little", signed=signed))

        self.deleted = False

    def __repr__(self) -> str:
        return self.value

    def __sizeof__(self) -> int:
        return size

    def __neg__(self) -> int:
        if not signed: raise ValueError("Cannot negate unsigned!")
        return -self.value

    def __pos__(self) -> int:
        return self.value

    def __abs__(self) -> int:
        if self.value < 0: return self.value * -1
        return self.value

    def __invert__(self) -> int:
        return ~self.value

    def __add__(self, other: object) -> int:
        if isinstance(other, int): return self.value + other
        return self.value + getattr(other, "value", 0)

    def __sub__(self, other: object) -> int:
        if isinstance(other, int): return self.value - other
        return self.value - getattr(other, "value", 0)

    def __mul__(self, other: object) -> int:
        if isinstance(other, int): return self.value * other
        return self.value * getattr(other, "value", 0)

    def __truediv__(self, other: object) -> float:
        if isinstance(other, int): return self.value / other
        return self.value / getattr(other, "value", 0)
    
    def __floordiv__(self, other: object) -> int:
        if isinstance(other, int): return self.value // other
        return self.value // getattr(other, "value", 0)

    def __mod__(self, other: object) -> int:
        if isinstance(other, int): return self.value % other
        return self.value % getattr(other, "value", 0)

    def __pow__(self, other: object, modulo=None) -> int:
        if isinstance(other, int): return self.value ** other
        return self.value ** getattr(other, "value", 0)

    def __lshift__(self, other: object) -> int:
        if isinstance(other, int): return self.value << other
        return self.value << getattr(other, "value", 0)

    def __rshift__(self, other: object) -> int:
        if isinstance(other, int): return self.value >> other
        return self.value << getattr(other, "value", 0)

    def __and__(self, other: object) -> int:
        if isinstance(other, int): return self.value & other
        return self.value & getattr(other, "value", 0)

    def __or__(self, other: object) -> int:
        if isinstance(other, int): return self.value | other
        return self.value | getattr(other, "value", 0)

    def __xor__(self, other: object) -> int:
        if isinstance(other, int): return self.value ^ other
        return self.value ^ getattr(other, "value", 0)

    def __iadd__(self, other: object) -> int:
        val = 0
        if isinstance(other, int):
            val = other
        else:
            val = getattr(other, "value", 0)
        self.value = self.value + val
        write_mem(self.value.to_bytes(size, "little", signed=signed), size, self.address)
        return self.value

    def __isub__(self, other: object) -> int:
        val = 0
        if isinstance(other, int):
            val = other
        else:
            val = getattr(other, "value", 0)
        self.value = self.value - val
        write_mem(self.value.to_bytes(size, "little", signed=signed), size, self.address)
        return self.value

    def __index__(self) -> int:
        return self.value

    def __del__(self) -> None:
        if not self.deleted:
            self.deleted = True
        return # C ends the stack frame for the func but we cannot do that

class char(CBaseType):
    """A single byte"""
    size = 1
    signed = True

class short(CBaseType):
    """2 bytes"""
    size = 2
    signed = True

class int_(CBaseType):
    """4 bytes"""
    size = 4
    signed = True

class long(CBaseType):
    """8 bytes"""
    size = 8
    signed = True

class unsigned_char(CBaseType):
    """unsigned char"""
    size = 1
    signed = False

class unsigned_short(CBaseType):
    """unsigned short"""
    size = 2
    signed = False

class unsigned_int(CBaseType):
    """unsigned int"""
    size = 4
    signed = False

class unsigned_long(CBaseType):
    """unsigned long"""
    size = 8
    signed = False

class void():
    """Just nothing, plain void"""
    def __init__(self) -> None:
        return # Incomplete type (Just a note, I mean like even in C it is incomplete, it means nothing!)

class pointer(CBaseType):
    """A 64-bit Pointer"""
    size = 8
    signed = True
    
    def __init__(self, obj: object, typ: type=void) -> None:
        self.typ = typ
        val = 0x0
        if isinstance(obj, int):
            val = obj
            if val < 0: raise ValueError("Address cannot be negative!")
        else:
            val = getattr(obj, "address", 0x0)
            print("[WARNING]: Object provided to pointer doesn't have any address! Defaulting to 0x0")

        super().__init__(val)
        self.ptr_addr = val # Another self var just for ease of use for the developer

    def deref(self) -> bytes:
        """Dereference the pointer. &pointer"""
        return read_mem(getattr(self.typ, "size", 8), self.value)

# typedefs for ease-of-use
ptr = pointer
Pointer = pointer
Void = void
Char = char
Short = short
Int = int_
Long = long
UChar = unsigned_char
UShort = unsigned_short
UInt = unsigned_int
ULong = unsigned_long
size_t = unsigned_long
Size_t = unsigned_long

class array():
    """C-Array, Example: 
    ``` c
        char myarray[5] // array of 5 characters/5 bytes
    ```
    """
    def __init__(self, typ: type, len: int) -> None:
        self.typ = typ
        self.len = len
        self.element_size = getattr(typ, "size", 1)
        self.total_size = self.element_size * len

        global heap_nextalloc
        base_addr = heap_nextalloc
        heap_nextalloc += self.total_size
        heap_registry[base_addr] = self.total_size
        self.address = base_addr

        write_mem(b"\x00"*self.total_size, self.total_size, self.address)

    def __getitem__(self, index: int) -> CBaseType:
        if not (0 <= index < self.len):
            raise IndexError(f"Array index [{index}] is out of range! 0-{self.len} available.")

        addr: int = self.address + (index * self.element_size)
        raw: bytes = read_mem(self.element_size, addr)
        data: int = int.from_bytes(raw, "little", signed=getattr(self.typ, "signed", True))
        ret = self.typ.__new__(self.typ)
        ret.value = data
        ret.address = addr
        ret.deleted = True # Temp
        return ret

    def __setitem__(self, index: int, value: Union[int, CBaseType]) -> None:
        if not (0 <= index < self.len):
            raise IndexError(f"Array index [{index}] is out of range! 0-{self.len} available.")

        val = value
        if isinstance(value, int) or isinstance(value, self.typ):
            if not isinstance(value, int):
                val = getattr(value, "value", 0)
            else:
                val = value
        else:
            raise ValueError(f"Trying to set array index [{index}] with a value of neither [{self.typ}] or [int] types!")

        addr: int = self.address + (index * self.element_size)
        size: int = self.element_size
        data: bytes = val.to_bytes(self.element_size, "little", signed=getattr(self.typ, "signed", True))
        write_mem(data, self.element_size, addr)

    def __len__(self) -> int:
        return self.len

    def __repr__(self) -> str:
        return f"<CArray {self.typ.__name__}[{self.len}] at {hex(self.address)} of size {self.total_size} bytes>"

class struct():
    """A C-Structure, uses format like -
    ```python
    format: dict = {
        "field1": {
            "type": long, # Type of field
            "value": None # Default value
        },
        "field2": {
            "type": pointer,
            "value": None,
            "ptr_type": short, # Pointer-Specific, Type of pointer
            "ptr_val": None # Pointer-Specific, Default Pointer type
        },
        "field3": {
            "type": array,
            "value": None,
            "array_type": char, # Array-Specific, Type of Array
            "array_len": 4 # Array-Specific, Length of Array
        }
    }
    ```
    """

    def __init__(self, structure: dict) -> None:
        self.struct = structure
        self.offsets = {}
        self.size = 0

        for name, info in self.struct.items():
            typ = info["type"]
            align_to = getattr(typ, "size", 1)
            self.size += align(self.size, align_to)
            self.offsets[name] = self.size
            
            field_size = 0

            # Handle
            # Arrays
            if typ == array:
                arr_typ = info.get("array_type", char)
                arr_len = info.get("array_len", 1)
                field_size = arr_typ * arr_len
            else:
                field_size = getattr(typ, "size", 1)
            self.size += field_size

        # Allocate
        global heap_nextalloc
        self.address = heap_nextalloc
        heap_nextalloc += self.size
        heap_registry[self.address] = self.size
        write_mem(b"\x00" * self.size, self.size, self.address)

        # write defaults
        for name, info in self.struct.items():
            if "value" in info and info["value"] is not None:
                self.__setattr__(name, info["value"])

    def __getattr__(self, name: str) -> Any:
        if name not in self.struct: raise ValueError(f"Unknown field [{name}]")

        info = self.struct[name]
        offset = self.offsets[name]
        typ = info["type"]

        if typ == array:
            arr_typ = info.get("array_type", char)
            arr_len = info.get("array_len", 1)
            arr_elementsize = getattr(arr_typ, "size", 1)
            arr = typ(arr_typ, arr_len)
            heap_nextalloc -= arr_len * arr_elementsize # Remove it's allocation
            arr.address = self.address + offset
            return arr
        elif typ == pointer:
            ptr_typ = info.get("ptr_type", void)
            raw = read_mem(pointer.size, self.address + offset)
            val = int.from_bytes(raw, "little", signed=getattr(ptr_typ, "signed", False))
            return typ(val)
        else:
            raw = read_mem(typ.size, self.address + offset)
            val = int.from_bytes(raw, "little", signed=getattr(typ, "signed", False))
            return typ(val)

    def __setattr__(self, name: str, value: Union[int, CBaseType, array, pointer]) -> None:
        if name in ("struct", "offsets", "size", "address"):
            super().__setattr__(name, value)
            return

        if name not in self.layout:
            raise AttributeError(f"No such field '{name}'")

        info = self.layout[name]
        offset = self.offsets[name]
        typ = info["type"]

        if typ == CArray:
            raise TypeError("Cannot directly assign to array field; use indexing.")
        elif typ == pointer:
            val = getattr(value, "address", value)
            write_mem(val.to_bytes(8, "little"), 8, self.address + offset)
        else:
            val = getattr(value, "value", value)
            write_mem(val.to_bytes(typ.size, "little", signed=typ.signed), typ.size, self.address + offset)

    def __repr__(self) -> str:
        field_str = []
        for name, info in self.layout.items():
            val = getattr(self, name)
            if isinstance(val, (CArray, pointer)):
                field_str.append(f"{name}={val}")
            else:
                field_str.append(f"{name}={val.value}")
        return f"<struct {', '.join(field_str)} at {hex(self.address)}>"

class enum:
    """C-style enum"""
    def __init__(self, name: str, fields: dict[str, int]):
        self.name = name
        self.fields = fields
        # Auto-fill missing values like C does
        value_counter = 0
        for k, v in list(fields.items()):
            if v is None:
                fields[k] = value_counter
            value_counter = fields[k] + 1

    def __getattr__(self, key):
        if key in self.fields:
            return self.fields[key]
        raise AttributeError(f"Enum {self.name} has no field {key}")

    def __repr__(self):
        items = ", ".join([f"{k}={v}" for k, v in self.fields.items()])
        return f"<enum {self.name}: {items}>"


