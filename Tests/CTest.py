import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.Extensions.C import *
from phardwareitk.Extensions.C_IO import *

if __name__ == "__main__":
    mem = input("Memory size? (in bytes, default 1024): ")
    mem = int(mem) if mem else 1024
    print(f"Allocating {mem} bytes of memory")
    reset_mem(mem)
    print("Creating a char")
    char = Char('H')
    print(char)
    print("Creating a Pointer to [char]")
    pointer = Pointer(Char, char)
    print(pointer)
    print("Making a string")
    string_ = make_string("Hello World")
    print(string_)
    print("Creating a short")
    short = Short(char.value)
    print(short)
    print("Mallocing 10 bytes")
    malloc_ = malloc(Size_t(10))
    print(malloc_)
    print("Freeing Malloc")
    try:
        free_ = free(malloc_)
        print(free_)
    except OSError as e:
        print("Failed to free malloc, error: ", e)
        print("Here memory to debug -")
        print(get_memory().ram)
    print("Freeing all")
    print("Can do del <class> but why when C has a full delete?")
    print("Running C full delete")
    full_delete()
    print("Running IO Test")
    print("Making file 'test.txt' in write mode")
    file_path = make_string("test.txt")
    file_mode = make_string("w")
    print(f"File path: {get_string(file_path)}")
    print(f"File mode: {get_string(file_mode)}")
    file_pointer = fopen(file_path, file_mode)
    if isinstance(file_pointer, int):
        print(f"Failed to open file, error code: {file_pointer}")
    else:
        print(f"File opened successfully: {file_pointer}")
        print("Writing to file")
        data = malloc(11)
        write(data, b"Hello World", 11)
        print("Wrote 'Hello World' to data buffer ->", data)
        print("Writing data to file")
        data.cast(Char)
        fwrite(data, 11, 1, file_pointer)
    fclose(file_pointer)
    print("File closed successfully")

