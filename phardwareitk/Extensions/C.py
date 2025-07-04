"""This file includes all classes to write Basic 'C' Code inside Python without the need of Cython."""
from typing import *
import sys
import os

MODULE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if not MODULE_DIR in sys.path:
	sys.path.append(MODULE_DIR)

# We need memory to work
from Memory import Memory as mem

# Basic Macros
NULL = 0
UNINITIALIZED: bytes = b'\xFF'

FALSE = 0
TRUE = 1

EXIT_SUCCESS = 0
EXIT_FALUIRE = 1

METADATA_MAGIC: bytes = int(0xF7F0FAF3).to_bytes(4, 'little')

base = 0x1
next_alloc = base

size = 64
memory = mem.Memory(64, 0, None, False, 0) # Defaults to 64 bytes as size

FREE_ADDR = {}

def reset_mem(size_:int, base_:int=0x0, debug:bool=False) -> None:
	"""Resets the memory but updates its size"""
	global size
	global memory
	global base
	global next_alloc
	if base_ != 0x0:
		base = base_
		next_alloc = base
	size = size_
	memory = mem.Memory(size, 0, None, debug, 0)
	FREE_ADDR.clear()

def get_next_alloc() -> int:
	global next_alloc
	return next_alloc

def set_next_alloc(value:int) -> None:
	global next_alloc
	next_alloc = value

def append_next_alloc(value:int) -> None:
	global next_alloc
	next_alloc += value + 8 # 8 bytes for metadata

def align(address:int, alignment:int) -> int: # To align to a specific address in memory
	if address % alignment == 0:
		return address
	return address + (alignment - (address % alignment))

def full_delete() -> None:
	"""Deletes everything from memory"""
	global size
	reset_mem(size)

def del_mem(addr:int, size_:int) -> None:
	"""NULLS/frees the specified memory block for the specified size"""
	global memory
	global size

	if addr > size:
		raise OSError("Trying to access memory outside of the virtual memory space. [ERROR:PHardwareITK:Extensions:C - del_mem]")

	memory.write_ram(b'\x00', addr, size_)
	FREE_ADDR[addr] = size_

def get_memory() -> mem.Memory:
	global memory
	return memory

def set_mem(addr:int, size_:int, data:bytes) -> None:
	"""Sets memory to specfied data"""
	global size
	global memory

	if addr > size:
		raise OSError("Trying to access memory outside of the virtual memory space. [ERROR:PHardwareITK:Extensions:C - set_mem]")

	memory.write_ram(METADATA_MAGIC + size_.to_bytes(4, 'little'), addr - 8, 8)
	memory.write_ram(data, addr, size_)

	if addr in list(FREE_ADDR.keys()):
		FREE_ADDR.pop(addr)

def get_mem(addr:int, size_:int) -> bytes:
	"""Gets memory"""
	global memory
	global size

	if addr > size:
		raise OSError("Trying to access memory outside of the virtual memory space. [ERROR:PHardwareITK:Extensions:C - get_mem]")

	return memory.get_ram(size_, addr)

def get_mem_size() -> int:
	global size
	return size

def metadata_verify(data:bytes) -> int:
	if not data == METADATA_MAGIC:
		return 1

	return 0

def get_size_metadata(addr:int) -> int:
	data: bytes = get_mem(addr, 8)
	if len(data) < 8:
		raise OSError(f"Not enough data to read metadata, expected 8 bytes, got less - {data}")

	magic = data[0:4]
	if not metadata_verify(magic) == 0:
		raise OSError(f"Falsly mapped data in memory, {data}")

	return int.from_bytes(data[4:8], 'little')

# Variables, and types
# The most basic needs
class Size_t:
	"""size_t"""

	def __init__(self, value:int) -> None:
		self.value = value #bytes
		self.bytes = value
		self.bits = value * 8
		self.kb = value / 1024
		self.mb = self.kb / 1024
		self.gb = self.mb / 1024
		self.tb = self.gb / 1024

	def __repr__(self) -> str:
		return f"{self.bytes}"

class Uint8_t:
	size = 1

	"""uint8_t"""
	def __init__(self, value:int=0) -> None:
		self.og_value = value

		if isinstance(value, str):
			if not len(value) == 0:
				value = ord(value)
			else:
				value = 0
		elif isinstance(value, bytes):
			value = int.from_bytes(value, 'big')

		if value > 0xFF:
			raise TypeError("Value exceeds 8 bits or 1 byte")

		self.value = value
		self.data = value.to_bytes(1, 'little')
		self.size = 1
		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		set_mem(self.address, self.size, self.data)

		self.deleted = False

	def __repr__(self) -> str:
		return f"{self.og_value}"

	def __del__(self) -> None:
		if getattr(sys, 'meta_path', None) is None:
			return  # Interpreter is shutting down; skip cleanup

		if self.deleted:
			return

		del_mem(self.address, self.size)

		self.deleted = True

class Uint16_t:
	size = 2

	"""uint16_t"""
	def __init__(self, value:int=0) -> None:
		self.og_value = value

		if isinstance(value, str):
			if not len(value) == 0:
				value = ord(value)
			else:
				value = 0
		elif isinstance(value, bytes):
			value = int.from_bytes(value, 'big')

		if value > 0xFFFF:
			raise TypeError("Value Exceeds 16 bits or 2 bytes")

		self.value = value
		self.data = value.to_bytes(2, 'little')
		self.size = 2
		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		set_mem(self.address, self.size, self.data)

		self.deleted = False

	def __repr__(self) -> str:
		return f"{self.og_value}"

	def __del__(self) -> None:
		if getattr(sys, 'meta_path', None) is None:
			return  # Interpreter is shutting down; skip cleanup

		if self.deleted:
			return

		del_mem(self.address, self.size)

		self.deleted = True

class Uint32_t:
	size = 4

	"""uint32_t"""
	def __init__(self, value:int=0) -> None:
		self.og_value = value

		if isinstance(value, str):
			if not len(value) == 0:
				value = ord(value)
			else:
				value = 0
		elif isinstance(value, bytes):
			value = int.from_bytes(value, 'big')

		if value > 0xFFFFFFFF:
			raise TypeError("Value Exceeds 32 bits or 4 bytes")

		self.value = value
		self.data = value.to_bytes(4, 'little')
		self.size = 4
		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		set_mem(self.address, self.size, self.data)

		self.deleted = False

	def __repr__(self) -> str:
		return f"{self.og_value}"

	def __del__(self) -> None:
		if getattr(sys, 'meta_path', None) is None:
			return  # Interpreter is shutting down; skip cleanup

		if self.deleted:
			return

		del_mem(self.address, self.size)

		self.deleted = True

class Uint64_t:
	size = 8

	"""uint64_t"""
	def __init__(self, value:int=0) -> None:
		self.og_value = value

		if isinstance(value, str):
			if not len(value) == 0:
				value = ord(value)
			else:
				value = 0
		elif isinstance(value, bytes):
			value = int.from_bytes(value, 'big')

		if value > 0xFFFFFFFFFFFFFFFF:
			raise TypeError("Value Exceeds 64 bits or 8 bytes")

		self.value = value
		self.data = value.to_bytes(8, 'little')
		self.size = 8
		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		set_mem(self.address, self.size, self.data)

		self.deleted = False

	def __repr__(self) -> str:
		return f"{self.og_value}"

	def __del__(self) -> None:
		if getattr(sys, 'meta_path', None) is None:
			return  # Interpreter is shutting down; skip cleanup

		if self.deleted:
			return

		del_mem(self.address, self.size)

		self.deleted = True

# Types of int
class Short(Uint16_t):
	"""short"""
	def __init__(self, value:int=0) -> None:
		super().__init__(value)

	def __repr__(self) -> str:
		return super().__repr__()

	def __del__(self) -> None:
		super().__del__()

class Long(Uint32_t):
	"""long"""
	def __init__(self, value:int=0) -> None:
		super().__init__(value)

	def __repr__(self) -> str:
		return f"Long of value [{self.value}] of size [{self.size}]"

	def __del__(self) -> None:
		super().__del__()

class Int(Uint32_t):
	"""int"""
	def __init__(self, value:int=0) -> None:
		super().__init__(value)

	def __repr__(self) -> str:
		return super().__repr__()

	def __del__(self) -> None:
		super().__del__()

# Chars and string access
class Char(Uint8_t):
	"""char"""
	def __init__(self, value:Union[str, int, bytes]='\0') -> None:
		super().__init__(value)

	def __repr__(self) -> str:
		return super().__repr__()

	def __del__(self) -> None:
		super().__del__()

# Pointers and void
class Void:
	"""void"""
	def __init__(self) -> None:
		self.size = 0
		self.value = None
		self.address = NULL # Void

	def __repr__(self) -> str:
		return "<void>"

class Pointer(Uint64_t):
	"""*<value>"""

	def __init__(self, type:object=Void, object:object=Void(), save:bool=False) -> None:
		self.type = type
		self.pointer_address = object

		if object == NULL:
			self.pointer_address = NULL

		if object is None:
			self.pointer_address = NULL

		if isinstance(object, int):
			pass
		elif isinstance(object, str):
			raise TypeError("Cannot create a pointer to a string (python)")
		elif isinstance(object, bytes):
			raise TypeError("Cannot create a pointer to bytes (python)")
		elif object is not None:
			self.pointer_address = object.address # A C.py file object

		self.obj = None
		self.save = save

		if save:
			self.obj = object

		super().__init__(self.pointer_address)
		# Don't Map * to memory

	def dereference(self) -> object:
		if isinstance(self.type, Void):
			raise TypeError("Cannot dereference a void pointer without casting it to another type.")

		if self.save:
			if self.obj is not None:
				return self.obj

		size = get_size_metadata(self.pointer_address - 8)

		data = get_mem(self.pointer_address, size)

		return data

	def cast(self, type:object) -> None:
		"""Casts a pointer to another type"""
		self.type = type

	def __repr__(self) -> str:
		return f"{self.pointer_address.to_bytes(8, 'little').hex()}"

	def __del__(self) -> None:
		super().__del__()

	@classmethod
	def __class_getitem__(cls, type_:object=Void, object_:object=None):
		class TypedPointer:
			size = 8
			object = object_
			type = type_
			def __new__(cls_, type:Void, object=None):
				return cls(type, object)

		return TypedPointer

# String access

def get_string(ptr:Pointer[Char]) -> str:
	"""Returns a string from an	memory address"""
	string = b""
	addr = ptr.pointer_address
	size = get_size_metadata(addr - 8)

	string = get_mem(addr, size).removesuffix(b'\x00\x00')  # Remove the null terminators

	return string.decode('utf-8')

CHAR_PTR = Pointer[Char]

# Arrays
class Array:
	"""<type>[<size>]"""
	def __init__(self, type:object, size:int) -> None:
		self.type = type
		self.size = size * type.size
		self.asize = size

		self.tsize = type.size

		self.array = []

		self.deleted = False

	def fill(self, data:bytes) -> None:
		for i in range(0, self.asize, self.tsize):
			self.array.append(self.type(data[i:self.tsize + i]))

	def __repr__(self) -> str:
		string = ""

		for obj in self.array:
			string += obj.__repr__()

		return string

	def __del__(self) -> None:
		if getattr(sys, 'meta_path', None) is None:
				return  # Interpreter is shutting down; skip cleanup

		if self.deleted: return
		for obj in self.array:
			obj.__del__()

		self.deleted = True

	@classmethod
	def __class_getitem__(cls, type_:object=None, size_:int=0):
		class TypedArray:
			size = size_
			type = type_
			def __new__(cls_, type:object, size:int):
				return cls(type, size)

		return TypedArray

# Funcs (Basic)
def sizeof(value:object) -> Size_t:
	if isinstance(value, int):
		return Size_t(Int(value).size)
	elif isinstance(value, str):
		return Size_t(make_string(value).size)
	elif isinstance(value, bytes):
		return Size_t(Uint64_t(value).size)
	else:
		return Size_t(value.size)

# Funcs (Memory)
def malloc(size:Union[int, Size_t]) -> Pointer[Void]:
	"""Allocate memory"""
	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(size, int):
		raise TypeError("Size is not a Size_t or a int.")

	for addr, sz in FREE_ADDR.items():
		if sz >= size + 8: # We found a free block
			FREE_ADDR.pop(addr) # We don't set the memory because C malloc doesn't either.
			return Pointer(Void, addr + 8)

	# ELSE
	addr = next_alloc
	append_next_alloc(size + 8)

	set_mem(addr, 8, METADATA_MAGIC + size.to_bytes(4, 'little')) # Set the metadata, we don't set the memory to unint because c doesnt either

	return Pointer(Void, addr + 8)

def free(ptr:Pointer) -> int:
	"""Free memory (doesn't delete pointer)"""
	addr = ptr.pointer_address
	size = get_mem_size()

	if addr > size:
		raise OSError("Trying to access memory outside of the virtual memory space. [ERROR:PHardwareITK:Extensions:C - free]")

	size = get_size_metadata(addr - 8)

	set_mem(addr, size, UNINITIALIZED * size)

	FREE_ADDR[addr] = size

	return 0

def calloc(nmemb:Union[int, Size_t], size:Union[int, Size_t]) -> Pointer[Void]:
	"""Allocate memory and set all values to 0"""
	if isinstance(nmemb, Size_t):
		nmemb = nmemb.bytes
	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(nmemb, int):
		raise TypeError("Error nmemb is not a Size_t or a int")
	elif not isinstance(size, int):
		raise TypeError("Error size is not a Size_t or a int")

	total_size = nmemb * size

	return malloc(total_size)

def realloc(ptr:Pointer[Void], size:Union[int, Size_t]) -> Pointer[Void]:
	"""Reallocate memory with new size"""
	# Free old memory
	free(ptr)

	# Allocate new memory
	return malloc(size)

def memcpy(dest: Pointer[Void], src: Pointer[Void], size: Union[int, Size_t]) -> Pointer[Void]:
	"""Copies [size] bytes from src to dest"""
	addr_dest = dest.pointer_address
	addr_src = src.pointer_address

	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(size, int):
		raise TypeError("Argument size must be a Size_t or a int")

	data = get_mem(addr_src, size)
	set_mem(addr_dest, size, data)
	return Pointer(Void, addr_dest)

def memmove(dest:Pointer[Void], src:Pointer[Void], size:Union[int, Size_t]) -> Pointer[Void]:
	"""Moves [size] bytes from src to dest"""
	addr_src = src.pointer_address

	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(size, int):
		raise TypeError("Argument size must be a Size_t or a int")

	memcpy(dest, src, size)
	set_mem(addr_src, size, UNINITIALIZED*size)

	return Pointer(Void, dest.pointer_address)

def memset(ptr:Pointer[Void], value:int, size:Union[int, Size_t]) -> Pointer[Void]:
	"""Sets [size] number of bytes of memory pointed to by [ptr] to the byte value [value]"""
	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(size, int):
		raise TypeError("Argument size must be a Size_t or a int")

	value = value.to_bytes(1, 'little')
	val = value * size

	set_mem(ptr.pointer_address, size, val)

	return ptr

def memchr(ptr:Pointer[Void], value:int, size:Union[int, Size_t]) -> Pointer[Void]:
	"""Finds the needed byte in memory"""
	addr = ptr.pointer_address
	cbyte = 0 # current addr
	searched_bytes = 0

	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(size, int):
		raise TypeError("Argument size must be a Size_t or a int")

	data = get_mem(addr, size)

	value = value.to_bytes(1, 'little')

	while True:
		if searched_bytes > size:
			return None

		if data[cbyte] == value:
			return Pointer(Void, addr + cbyte)

def memcmp(ptr1:Pointer[Void], ptr2:Pointer[Void], size:Union[int, Size_t]) -> int:
	"""Compares two data in memory"""
	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(size, int):
		raise TypeError("Argument size must be a Size_t or a int")

	addr1 = ptr1.pointer_address
	addr2 = ptr2.pointer_address
	data1 = get_mem(addr1, size)
	data2 = get_mem(addr2, size)

	if data1 == data2:
		return 0
	else:
		return 1

def write(ptr:Pointer[Void], data:bytes, size:Union[int, Size_t]) -> int:
	"""Writes data to memory"""
	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(size, int):
		raise TypeError("Argument size must be a Size_t or a int")

	set_mem(ptr.pointer_address, size, data)

	return 0

def read(ptr:Pointer[Void], size:Union[int, Size_t]) -> bytes:
	"""Reads data from memory"""
	if isinstance(size, Size_t):
		size = size.bytes

	if not isinstance(size, int):
		raise TypeError("Argument size must be a Size_t or a int")

	addr = ptr.pointer_address
	data = get_mem(addr, size)

	return data

# String creation
def make_string(value:str) -> Pointer[Char]:
	"""Makes a char*"""

	if not isinstance(value, str):
		raise TypeError("Value must be a [str]")

	if not value.endswith('\x00\x00'):
		value += '\x00\x00'

	# Make a list of Char
	out = malloc(len(value))

	out.cast(Char)

	write(out, value.encode('utf-8'), len(value)) # Write the string to memory

	return out # char* is basically the pointer to the first char in a string

# Structs
class Struct:
	"""struct {...}"""

	def __init__(self, structure:dict) -> None:
		"""Format:
			{
				'<Name>': {
					'type': <type in form of one of the class here>,
					'value': <value>
				}
			}
		"""
		self.structure = structure
		self.size = 0
		self.value = NULL

		self.data = [] # Data of the struct, Format = (<name>, <size>)

		self.get_size() # Set the size

		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		set_mem(self.address, self.size, UNINITIALIZED * self.size)

		self.deleted = False

		for key, value in self.structure.items():
			self.data.append((key, sizeof(value['type']).bytes))

	def access(self, name:str) -> Any:
		"""Returns the value of the object"""
		val = None

		try:
			val = self.structure[name]['value']
		except Exception:
			return -1

		return val

	def get_offset(self, name:str) -> int:
		"""Returns the offset of the object"""
		offset = 0

		for key, value in self.data:
			if key == name:
				return offset

			offset += value + 8 # 8 bytes for metadata

	def set(self, name:str, value:object) -> int:
		"""Sets the new value of a part of the struct. NOTE: The new value must be of the old defined type"""
		t = None

		try:
			t = self.structure[name]['type']
		except Exception:
			return -1

		if not isinstance(value, t):
			return -2

		try:
			self.structure[name]['value'] = value
		except Exception:
			return -3

		# We need to move the data to the struct
		offset = self.get_offset(name)
		set_mem(self.address + offset, value.size, get_mem(value.address, value.size))
		# remove old data
		del_mem(value.address - 8, value.size + 8)

		return 0

	def get_size(self) -> int:
		self.size = 0
		for key, value in self.structure.items():
			self.size += sizeof(value['type']).bytes

		return self.size

	def fill_b(self, data:bytes, byteorder:str='big') -> int:
		"""Fills the entire struct by the provided value (bytes)"""
		self.get_size()

		if len(data) < self.size:
			return -1 # Not enough data

		index = 0
		for name, field in self.structure.items():
			field_size = field["value"].size
			field_data = data[index : index + field_size]

			field_type = field['type']
			field_value = int.from_bytes(field_data, byteorder)

			if isinstance(field_type, Char):
				field_value = Char(field_data.decode('utf-8'))
			elif isinstance(field_type, Pointer):
				if isinstance(field_type.type, Char):
					field_value = make_string(field_data.decode('utf-8'))
				elif isinstance(field_type.type, Array):
					field_value = field_type.type
					field_value.fill(field_data)
					field_value = field_type(field_value)
				elif isinstance(field_type.type, Void):
					# void* means it can point to anything
					# We are assuming anything
					field_value = field_type(field_type.type())
			elif isinstance(field_type, Array):
				field_value = field_type
				field_value.fill(field_data) # Fill the array with the data
			elif isinstance(field_type, Void):
				# Void in C means anything/nothing
				# We are assuming anything
				field_value = field_type()

			field_value = field_value.data

			self.set(name, field_value)

			index += field_size

	def fill_f(self, file:TextIO, byteorder:str='big') -> int:
		"""Fills the struct from a file"""
		self.get_size()
		data = file.read(self.size)
		return self.fill_b(data, byteorder)

	def write_b(self, buffer_:Pointer[Void]) -> int:
		if self.size < 1:
			return -1 # Size = 0

		addr = buffer_.pointer_address

		self.get_size()
		write(buffer_, get_mem(self.address, self.size), self.size) # Basically memcpy but worse because memcpy can't work properly here.
		return 0

	def dereference(self, ptr:Pointer[Void]) -> None:
		"""Dereferences a pointer to the struct and returns the struct object."""
		self.get_size()
		del_mem(self.address, self.size)
		self.address = ptr.pointer_address
		self.fill_b(get_mem(self.address, self.size))

	def __del__(self) -> None:
		if getattr(sys, 'meta_path', None) is None:
			return  # Interpreter is shutting down; skip cleanup

		if self.deleted:
			return # Already deleted

		del_mem(self.address, self.size)
		self.deleted = True

		# Free the objects
		for key, value in self.structure.items():
			val = value['value']
			if not val is None:
				del val

	@classmethod
	def __class_getitem__(cls, struct:dict={}, size_:int=0):
		class TypedStruct:
			structure = struct
			size = size_
			def __new__(cls_, structure:dict):
				return cls(structure)

		return TypedStruct

def dereference_struct(ptr:Pointer[Struct], structure:dict) -> Struct:
	"""Dereferences a pointer to a struct and returns the struct object.

	Args:
		ptr (Pointer[Struct]): Pointer to the struct object
		structure (dict): The struct definition

	Returns:
		Struct: The struct object
	"""
	return Struct(structure).dereference(ptr)
