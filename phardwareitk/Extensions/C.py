"""This file includes all classes to write Basic 'C'/'C++' Code inside Python without the need of Cython."""
from typing import *
import sys

# Constants
NULL = 0

# Variables, and types

class Pointer:
    """A generic pointer class that holds a reference to a variable."""

    def __init__(self, value):
        """Initializes the pointer with a given value."""
        self.value = value
        self.parent = None  # Optional: Track original variable

    def __repr__(self):
        return f"<Pointer to {type(self.value).__name__} at {hex(id(self))}>"

class Char:
    """Represents a character. [1 byte]"""
    def __init__(self, value:Union[str, int]) -> None:
        if not isinstance(value, str):
            raise TypeError("A [char] can only store single characters, not numbers, or any other type.")

        if not len(value) == 1:
            raise TypeError("A [char] can only store 1 byte.")

        self.value:int = ord(value)
        self.printable_value:str = value
        self.size:int = len(value)

    def __repr__(self):
        return f"Character [{self.printable_value}] of size [{self.size}]"

class Short:
    """Stores small integers [-32768 to 32767]
    """
    def __init__(self, value:int) -> None:
        if not isinstance(value, int):
            raise TypeError("A [short] can only store integers.")

        if value > 32676 or value < -32768:
            raise TypeError("A [short] can only store from [-32768] to [32676].")

        self.value:int = value
        self.size:int = sys.getsizeof(value)

    def __repr__(self):
        return f"Short [{self.value}] of size [{self.size}]."

class Long:
    """Larger Integer type.
    """
    def __init__(self, value:int):
        if not isinstance(value, int):
            raise TypeError("[long] can only store integers.")

        self.value = value
        self.size = sys.getsizeof(value)

    def __repr__(self):
        return f"Long of value [{self.value}] of size [{self.size}]"

class Signed:
    """Explicit declaration of an var being able to store both negative and positive values."""
    def __init__(self, value:Union[Char, int, Short, Long]):
        if not isinstance(value, Char) and (not isinstance(value, int) and (not isinstance(value, Short) and not isinstance(value, Long))):
            raise TypeError("[signed] only works on [int].")

        self.value:int = value
        self.size:int = 0
        self.type = ""
        if isinstance(value, int):
            self.type = "Int"
            self.size = sys.getsizeof(value)
        elif isinstance(value, Char):
            self.type = "Char"
            self.size = value.size
            self.value = value.value
        elif isinstance(value, Short):
            self.type = "Short"
            self.size = value.size
            self.value = value.value
        elif isinstance(value, Long):
            self.type = "Long"
            self.size = value.size
            self.value = value.value

    def __repr__(self):
        return f"Signed {self.type} of value [{self.value}] of size [{self.size}]"

class Unsigned:
    """Explicit declaration of an var being able to store only non-negative values [0, 1, 2, ...]."""
    def __init__(self, value:Union[Char, int, Short, Long]):
        if not isinstance(value, Char) and (not isinstance(value, int) and (not isinstance(value, Short) and not isinstance(value, Long))):
            raise TypeError("[unsigned] only works on [int].")

        self.value:int = value
        self.size:int = 0
        self.type = ""
        if isinstance(value, int):
            self.type = "Int"
            self.size = sys.getsizeof(value)
        elif isinstance(value, Char):
            self.type = "Char"
            self.size = value.size
            self.value = value.value
        elif isinstance(value, Short):
            self.type = "Short"
            self.size = value.size
            self.value = value.value
        elif isinstance(value, Long):
            self.type = "Long"
            self.size = value.size
            self.value = value.value

        if value < 0:
            raise TypeError("[unsigned] can only store positive values.")

    def __repr__(self):
        return f"Unsigned {self.type} of value [{self.value}] of size [{self.size}]"
