import sys
import os

modpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
if not modpath in sys.path:
    sys.path.insert(0, modpath)

from phardwareitk.Extensions.C import *
from phardwareitk.Extensions.C.stdlib import *

print("Initializing with 128 bytes...")
initialize(128)
print("Setting up stack frame...")
push_frame()
print("Creating a String!")
string = cstring("Hello from C!")
print("String:", string)
print("Dereferenced String:", string.deref().decode("utf-8"))
print("mallocing 5 bytes")
_ptr = malloc(size_t(5))

if _ptr is None:
    print("Malloc Failed!")
    exit(Int(-1))

print("Malloc:", _ptr)
print("Freeing Memory!")
free(_ptr)

print("Making an Array!")
arr = array(char, 32)
arr[0] = char('A')
arr[1] = char('B')

print("Array:\n\t", arr)
print("\nArr[0]:", arr[0])
print("Popping stack frame...")
pop_frame()

print("Bye!")
