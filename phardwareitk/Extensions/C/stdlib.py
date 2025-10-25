"C-stdlib. Python - C - Standard Library"

from phardwareitk.Extensions import C
from typing import Union, Optional, Callable
import sys
import os
import random

_free_list: list[tuple[int, int]] = []
_atexit_funcs: list[Callable] = []

# Memory
def malloc(size_: C.size_t) -> Optional[C.pointer[C.void]]:
    """Allocate size on heap"""
    global _free_list
    
    size = C.align(size_.value, 2)

    for i, (addr, fsize) in enumerate(_free_list):
        if fsize >= size:
            C._heap_registry[addr] = size
            if fsize > size:
                new_free = (addr + size, fsize - size)
                _free_list[i] = new_free
            else:
                _free_list.pop(i)
            return C.pointer(addr, C.void)

    if size + C._heap_nextalloc > C._heap_size:
        return None

    addr = C._heap_nextalloc
    C._heap_registry[addr] = size
    C._heap_nextalloc += size
    return C.pointer(addr, C.void)

def free(ptr: C.pointer) -> None:
    """Frees the allocated heap memory for later use"""
    global _free_list
    addr = ptr.ptr_addr

    if not addr in C._heap_registry:
        raise OSError(f"Unknown Address {hex(addr)} for freeing!")

    size = C._heap_registry[addr]
    del C._heap_registry[addr]
    _free_list.append((addr, size))
    # Merge adjacent free addr
    # Sort by address
    _free_list.sort(key=lambda x: x[0])
    merged = []
    last_addr, last_size = _free_list[0]

    for addr, size in _free_list[1:]:
        if addr == last_addr + last_size:
            # Adjacent → merge
            last_size += size
        else:
            merged.append((last_addr, last_size))
            last_addr, last_size = addr, size

    merged.append((last_addr, last_size))
    _free_list = merged

def realloc(ptr: C.pointer, new_size: C.size_t) -> Optional[C.pointer[C.void]]:
    """Reallocate on the heap"""
    free(ptr)
    return malloc(new_size)

def calloc(nmemb: C.size_t, size: C.size_t) -> Optional[C.pointer[C.void]]:
    """Allocate specified number of members of specified size"""
    total_size = C.size_t(nmemb * size)
    new_ptr = malloc(total_size)
    if new_ptr is not None:
        offset = new_ptr.ptr_addr
        for i in range(nmemb.value):
            C.write_mem(b"\x00"*size.value, size.value, offset)
            offset += size.value
    return new_ptr

EXIT_SUCCESS = 0
EXIT_FALUIRE = 1

NULL = 0 # ((void*)0)

# Process Control
def abort() -> None:
    """Halts the program directly"""
    os.abort()

def exit(status: C.Int) -> None:
    """Exits the program"""
    global _atexit_funcs
    for func in _atexit_funcs:
        func()
    sys.exit(status.value)

def _Exit(status: C.Int) -> None:
    """Like exit but with minimal cleanup and, it doesn't call atexit"""
    os._exit(status.value)

def atexit(func: Callable) -> None:
    """Runs the function provided on exit of program"""
    global _atexit_funcs
    _atexit_funcs.insert(0, func)

# System

def getenv(name: C.pointer[C.char]) -> C.pointer[C.char]:
    """Gets Environment Variable"""
    pyname = name.deref().decode("utf-8")
    val = os.getenv(pyname)
    if val is None:
        return C.pointer(NULL, C.void)
    return C.cstring(val)

def system(command: C.pointer[C.char]) -> C.Int:
    """Runs a system command"""
    out = os.system(command.deref().decode("utf-8"))
    return C.Int(out)

def abs_(j: C.Int) -> C.Int:
    return C.Int(abs(j.value))

def labs(j: C.Int) -> C.Int:
    return C.Int(abs(j.value))

def div_(numer: C.Int, denom: C.Int):
    class div_t:
        quot: int
        rem: int
        def __init__(self, q, r):
            self.quot, self.rem = q, r
    return div_t(numer.value // denom.value, numer.value % denom.value)

#  Conversion Routines

def atoi(nptr: C.pointer[C.char]) -> C.Int:
    s = nptr.deref().decode("utf-8")
    return C.Int(int(s.strip() or 0))

def atof(nptr: C.pointer[C.char]) -> C.double:
    s = nptr.deref().decode("utf-8")
    try:
        return C.double(float(s.strip()))
    except ValueError:
        return C.double(0.0)

def atol(nptr: C.pointer[C.char]) -> C.Int:
    s = nptr.deref().decode("utf-8")
    try:
        return C.Int(int(s.strip()))
    except ValueError:
        return C.Int(0)

# Random

def srand(seed: C.Int) -> None:
    random.seed(seed.value)

def rand() -> C.Int:
    return C.Int(random.randint(0, 32767))

# Search & Sort

def qsort(base: C.pointer[C.array], nmemb: C.size_t, size: C.size_t, compar: Callable): pass

def bsearch(key: C.pointer[C.char], base: C.pointer[C.array], nmemb: C.size_t, size: C.size_t, compar: Callable): pass

# Multibyte / Wide Char

def mbstowcs(pwcs, s, n): pass
def wcstombs(s, pwcs, n): pass
def mbtowc(pwc, s, n): pass
def wctomb(s, wc): pass
def mblen(s, n): pass
