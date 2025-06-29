"""This file includes all classes to write Basic 'C'/'C++' Code inside Python without the need of Cython."""
from typing import *
import sys

# Constants
NULL = 0

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
	def __init__(self, value) -> None:
		self.og_value = value

		if isinstance(value, str):
			if not len(value) == 0:
				value = ord(value)
			else:
				value = 0
		elif isinstance(value, bytes):
			value = int.from_bytes(value, 'big')

		if not value >= 0xF:
			raise TypeError("Value exceeds 8 bits or 1 byte")

		self.value = value
		self.size = 0xF

	def __repr__(self) -> str:
		return f"{self.og_value}"

class Uint16_t:
	"""uint16_t"""
	def __init__(self, value) -> None:
		self.og_value = value

		if isinstance(value, str):
			if not len(value) == 0:
				value = ord(value)
			else:
				value = 0
		elif isinstance(value, bytes):
			value = int.from_bytes(value, 'big')

		if not value >= 0xFF:
			raise TypeError("Value Exceeds 16 bits or 2 bytes")

		self.value = value
		self.size = 0xFF

	def __repr__(self) -> str:
		return f"{self.og_value}"

class Uint32_t:
	"""uint32_t"""
	def __init__(self, value) -> None:
		self.og_value = value

		if isinstance(value, str):
			if not len(value) == 0:
				value = ord(value)
			else:
				value = 0
		elif isinstance(value, bytes):
			value = int.from_bytes(value, 'big')

		if not value >= 0xFFFF:
			raise TypeError("Value Exceeds 32 bits or 4 bytes")

		self.value = value
		self.size = 0xFFFF

	def __repr__(self) -> str:
		return f"{self.og_value}"

class Uint64_t:
	"""uint64_t"""
	def __init__(self, value) -> None:
		self.og_value = value

		if isinstance(value, str):
			if not len(value) == 0:
				value = ord(value)
			else:
				value = 0
		elif isinstance(value, bytes):
			value = int.from_bytes(value, 'big')

		if not value >= 0xFFFFFFFF:
			raise TypeError("Value Exceeds 64 bits or 8 bytes")

		self.value = value
		self.size = 0xFFFFFFFF

	def __repr__(self) -> str:
		return f"{self.og_value}"

# Types of int
class Short(Uint16_t):
	"""short"""
	def __init__(self, value:int) -> None:
		super().__init__(value)

	def __repr__(self) -> str:
		return super().__repr__()

class Long(Uint32_t):
	"""long"""
	def __init__(self, value:int) -> None:
		super().__init__(value)

	def __repr__(self) -> str:
		return f"Long of value [{self.value}] of size [{self.size}]"

class Int(Uint32_t):
	"""int"""
	def __init__(self, value:int) -> None:
		super().__init__(value)

	def __repr__(self) -> str:
		return super().__repr__()

# Chars and strings
class Char(Uint8_t):
	"""char"""
	def __init__(self, value:Union[str, int, bytes]) -> None:
		super().__init__(value)

	def __repr__(self) -> str:
		return super().__repr__()

# Signed and Unsigned
class Signed:
	"""signed"""
	def __init__(self, value) -> None:
		self.value:int = value

	def __repr__(self) -> str:
		return super().__repr__()

class Unsigned:
	"""unsigned"""
	def __init__(self, value) -> None:
		self.value = value

		if value.value < 0:
			raise TypeError("Negative value in unsigned")

	def __repr__(self) -> str:
		return super().__repr__()

# Pointers and void
class Void:
	"""void"""
	def __init__(self) -> None:
		self.size = 0
		self.value = None

	def __repr__(self) -> str:
		return "<void>"

class Pointer(Uint64_t):
	"""*<value>"""

	def __init__(self, value) -> None:
		self.pointer = value
		super().__init__(id(value))

	def __repr__(self) -> str:
		return super().__repr__()

# Funcs (Basic)
def sizeof(value:object):
	if isinstance(value, int):
		return Size_t(Int(value).size)
	elif isinstance(value, str):
		return Size_t(Pointer(list(value)).size)
	elif isinstance(value, bytes):
		return Size_t(Uint64_t(value).size)
	else:
		return Size_t(value.size)

# Structs
class Struct:
	"""A generic C struct"""

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

	def size(self) -> Size_t:
		self.size = 0
		for key, value in self.structure.items():
			self.size += sizeof(value['value'])

	def fill(self, data:bytes) -> int:
		"""Fills the entire struct by the provided value"""


