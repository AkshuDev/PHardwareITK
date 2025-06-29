"""This file includes all classes to write Basic 'C' Code inside Python without the need of Cython."""
from typing import *
import sys

# Constants
NULL = 0
FALSE = 0
TRUE = 1

EXIT_SUCCESS = 0
EXIT_FALUIRE = 1

# Maps for handling Memory and such because Python doesn't let you derefernece a pointer and has wierd management for memory
# The base (uint64_t)
BASE: int = 0x600000000000 # High enough to avoid kernel, common for heap/mmap in linux, leavs plenty of space below for code, stack, and libs
global next_alloc

next_alloc = BASE
MEMORY_MAP: dict = {}
FREE_LIST: list = []
ALLOC_TABLE: dict = {}

def get_next_alloc() -> int:
    global next_alloc
    return next_alloc

def set_next_alloc(value:int) -> None:
    global next_alloc
    next_alloc = value

def append_next_alloc(value:int) -> None:
	global next_alloc
	next_alloc += value

def align(address:int, alignment:int) -> int: # To align to a specific address in memory
    if address % alignment == 0:
        return address
    return address + (alignment - (address % alignment))

def full_delete(objects:list[object]) -> None:
	"""Deletes all objects in a list"""
	for obj in objects:
		# Remove them from the memory map
		del MEMORY_MAP[obj.address]

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
		self.size = 1
		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		MEMORY_MAP[self.address] = self
		ALLOC_TABLE[self.address] = self.size

		self.deleted = False

	def __repr__(self) -> str:
		return f"{self.og_value}"

	def __del__(self) -> None:
		if self.deleted:
			return

		FREE_LIST.append((self.address, self.size))
		MEMORY_MAP.pop(self.address)
		ALLOC_TABLE.pop(self.address)

		self.deleted = True

class Uint16_t:
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
		self.size = 2
		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		MEMORY_MAP[self.address] = self
		ALLOC_TABLE[self.address] = self.size
		self.deleted = False

	def __repr__(self) -> str:
		return f"{self.og_value}"

	def __del__(self) -> None:
		if self.deleted:
			return

		FREE_LIST.append((self.address, self.size))
		MEMORY_MAP.pop(self.address)
		ALLOC_TABLE.pop(self.address)

		self.deleted = True

class Uint32_t:
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
		self.size = 4
		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		MEMORY_MAP[self.address] = self
		ALLOC_TABLE[self.address] = self.size

		self.deleted = False

	def __repr__(self) -> str:
		return f"{self.og_value}"

	def __del__(self) -> None:
		if self.deleted:
			return

		FREE_LIST.append((self.address, self.size))
		MEMORY_MAP.pop(self.address)
		ALLOC_TABLE.pop(self.address)

		self.deleted = True

class Uint64_t:
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
		self.size = 8
		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		MEMORY_MAP[self.address] = self
		ALLOC_TABLE[self.address] = self.size

		self.deleted = False

	def __repr__(self) -> str:
		return f"{self.og_value}"

	def __del__(self) -> None:
		if self.deleted:
			return

		FREE_LIST.append((self.address, self.size))
		MEMORY_MAP.pop(self.address)
		ALLOC_TABLE.pop(self.address)

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

def get_string(address:Uint64_t) -> str:
	"""Returns a string from an	memory address"""
	string = ""
	addr = address.value

	if not isinstance(MEMORY_MAP[address.value], Char):
		return ""

	while True: # Because if we create another Char object it will map itself to memory again
		if not isinstance(MEMORY_MAP[addr], Char):
			break

		if not MEMORY_MAP[addr].og_value == '\0':
			break

		string += MEMORY_MAP[addr].og_value
		addr += align(addr + 1, MEMORY_MAP[addr].size)

	return string

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

	def __init__(self, type:Void, object:object=None) -> None:
		self.type = type
		self.pointer_address = object

		if object == NULL:
			self.pointer_address = NULL

		if object == None:
			self.pointer_address = NULL

		if isinstance(object, int):
			pass
		elif isinstance(object, str):
			raise TypeError("Cannot create a pointer to a string (python)")
		elif isinstance(object, bytes):
			raise TypeError("Cannot create a pointer to bytes (python)")
		else:
			self.pointer_address = object.address # A C.py file object

		super().__init__(self.pointer_address)
		# Don't Map * to memory

	def derefernce(self) -> object:
		if isinstance(self.type, Void):
			raise TypeError("Cannot dereference a void pointer without casting it to another type.")

		return MEMORY_MAP[self.value]

	def cast(self, type:object) -> None:
		"""Casts a pointer to another type"""
		self.type = type

	def __repr__(self) -> str:
		if isinstance(self.type, Char):
			return f"{get_string(Uint64_t(self.value))}"
		else:
			return super().__repr__()

	def __del__(self) -> None:
		super().__del__()

	@classmethod
	def __class_getitem__(cls, type_):
		return cls(type_, NULL)

# String creation
def string(value:str) -> Pointer[Char]:
	"""Makes a char*"""

	if not isinstance(value, str):
		raise TypeError("Value must be a [str]")

	if not value.endswith('\0'):
		value += '\0'

	# Make a list of Char
	string = []
	for c in value:
		string.append(Char(c))

	return Pointer(Char, string[0]) # char* is basically the pointer to the first char in a string

# Arrays
class Array:
	"""<type>[<size>]"""
	def __init__(self, type:object, size:int) -> None:
		self.type = type
		self.size = size

		self.tsize = type.size

		self.array = []

		self.deleted = False

	def fill(self, data:bytes) -> None:
		for i in range(self.size, step=self.tsize):
			self.array.append(self.type(data[i]))

	def __repr__(self) -> str:
		string = ""

		for obj in self.array:
			string += obj.__repr__()

		return string

	def __del__(self) -> None:
		if self.deleted: return
		for obj in self.array:
			obj.__del__()

		self.deleted = True

# Funcs (Basic)
def sizeof(value:object) -> Size_t:
	if isinstance(value, int):
		return Size_t(Int(value).size)
	elif isinstance(value, str):
		return Size_t(string(value).size)
	elif isinstance(value, bytes):
		return Size_t(Uint64_t(value).size)
	else:
		return Size_t(value.size)

# Funcs (Memory)
def malloc(size:Size_t) -> Pointer[Void]:
	for i, (addr, block_size) in enumerate(FREE_LIST):
		if block_size >= size.bytes: # We found a free block
			FREE_LIST.pop(i)
			ALLOC_TABLE[addr] = size.bytes # Update size of the block
			MEMORY_MAP[addr] = Void()
			return Pointer(Void, addr)

	# ELSE
	addr = next_alloc
	MEMORY_MAP[addr] = Void()
	ALLOC_TABLE[addr] = size.bytes
	append_next_alloc(size.bytes)
	return Pointer(Void, addr)

def free(ptr:Pointer[Void]) -> int:
	"""Free memory (doesn't delete pointer)"""
	addr = ptr.pointer_address

	if addr in list(MEMORY_MAP.keys()):
		try:
			FREE_LIST.append((addr, ALLOC_TABLE[addr]))
			ALLOC_TABLE.pop(addr)
			MEMORY_MAP.pop(addr)
		except KeyError:
			return -1 # Memory already freed
		return 0
	else:
		return -4

def calloc(nmemb:Size_t, size:Size_t) -> Pointer[Void]:
	"""Allocate memory and set all values to 0"""
	total_size = nmemb.bytes * size.bytes

	return malloc(Size_t(total_size))

def realloc(ptr:Pointer[Void], size:Size_t) -> Pointer[Void]:
	"""Reallocate memory with new size"""
	# Free old memory
	free(ptr)

	# Allocate new memory
	return malloc(size)

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

		self.get_size() # Set the size

		self.address = align(next_alloc, self.size)
		append_next_alloc(self.size)

		MEMORY_MAP[self.address] = self
		ALLOC_TABLE[self.address] = self.size

	def access(self, name:str) -> Any:
		"""Returns the value of the object"""
		val = None

		try:
			val = self.structure[name]['value']
		except Exception:
			return -1

		return val

	def set(self, name:str, value) -> int:
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

		return 0

	def get_size(self) -> Size_t:
		self.size = 0
		for key, value in self.structure.items():
			self.size += sizeof(value['value'])

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
					field_value = string(field_data.decode('utf-8'))
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

			self.set(name, field_value)

			index += field_size

	def fill_f(self, file:TextIO, byteorder:str='big') -> int:
		"""Fills the struct from a file"""
		self.get_size()
		data = file.read(self.size)
		return self.fill_b(data, byteorder)

	def __del__(self) -> None:
		MEMORY_MAP.pop(self.address)
		ALLOC_TABLE.pop(self.address)
		FREE_LIST.append((self.address, self.size))

		# Free the objects
		for key, value in self.structure.items():
			val = value['value']
			if not val is None:
				del val

