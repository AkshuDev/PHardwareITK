import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.Extensions.C import *

if __name__ == "__main__":
    print("Creating a char")
    char = Char('H')
    print(char)
    print("Creating a Pointer to [char]")
    pointer = Pointer(Char, char)
    print(pointer)
    print("Making a string")
    string_ = string("Hello World")
    print(string_)
    print("Creating a short")
    short = Short(char.value)
    print(short)
    print("Mallocing 10 bytes")
    malloc_ = malloc(Size_t(10))
    print(malloc_)
    print("Freeing Malloc")
    free_ = free(malloc_)
    print(free_)
    print("All the allocs")
    print(ALLOC_TABLE)
    print("All the frees")
    print(FREE_LIST)
    print("Full memory")
    print(MEMORY_MAP)
    print("Freeing all")
    print("Doesn't free memory instantly because they are still stored in memory")
    print("Running C full delete")
    full_delete([char, pointer, string_, short, malloc_])