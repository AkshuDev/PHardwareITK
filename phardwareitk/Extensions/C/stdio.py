from typing import *
import os
import sys

from phardwareitk.Extensions import C
from phardwareitk.Extensions.C import stdlib

do_print_exception = False

def set_exception_print(val:bool) -> None:
    """True for printing exception, False for otherwise"""
    global do_print_exception
    do_print_exception = val
    
def print_exception(exception) -> None:
    """Prints exception provided based on the do_print_exception, whose value is setted by set_exception_print function"""
    global do_print_exception
    if do_print_exception:
        print(exception)

SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2

_IO_FILE = {
    "_IO_read_ptr": {
        "type": C.pointer,
        "ptr_type": C.char,
        "value": None
    },
    "_IO_read_end": {
        "type": C.pointer,
        "ptr_type": C.char,
        "value": None
    },
    "_IO_read_base": {
        "type": C.pointer,
        "ptr_type": C.char,
        "value": None
    },
    "_IO_write_base": {
        "type": C.pointer,
        "ptr_type": C.char,
        "value": None
    },
    "_IO_write_ptr": {
        "type": C.pointer,
        "ptr_type": C.char,
        "value": None
    },
    "_IO_write_end": {
        "type": C.pointer,
        "ptr_type": C.char,
        "value": None
    },
    "_IO_buf_base": {
        "type": C.pointer,
        "ptr_type": C.char,
        "value": None
    },
    "_IO_buf_end": {
        "type": C.pointer,
        "ptr_type": C.char,
        "value": None
    },
    "_fileno": {
        "type": C.Int,
        "value": None
    },
    "_blksize": {
        "type": C.Int,
        "value": None
    }
}
"""struct _IO_FILE {
   char  *_IO_read_ptr;   /* Current read pointer */
   char  *_IO_read_end;   /* End of get area. */
   char  *_IO_read_base;  /* Start of putback and get area. */
   char  *_IO_write_base; /* Start of put area. */
   char  *_IO_write_ptr;  /* Current put pointer. */
   char  *_IO_write_end;  /* End of put area. */
   char  *_IO_buf_base;   /* Start of reserve area. */
   char  *_IO_buf_end;   /* End of reserve area. */
   int   _fileno;
   int   _blksize;
};

typedef struct _IO_FILE FILE;"""

FILE = C.struct[_IO_FILE]

def _get_string(ptr: Union[C.pointer[C.char], str, None]) -> str:
    if ptr is None: return None
    if isinstance(ptr, str): return ptr
    return ptr.deref()

def fopen(path:Union[C.pointer[C.char], str], mode:Union[C.pointer[C.char], str]) -> Union[C.pointer[FILE], C.Int]:
    """fopen - Open a file and return a FILE struct pointer

    Arguments:
        path (char*):
            Path to the file
        mode (char*):
            Mode to open the file with (e.g. 'r', 'w', 'rb', ...)

    Returns: Pointer to FILE (_IO_FILE) struct or -1 on failure, -2 on file not found, -3 on permission error"""
    C.push_frame()
    filename = _get_string(path)
    mode = _get_string(mode)

    if "b" not in mode:
        mode += "b"

    fd = None

    try:
        fd = open(filename, mode)
    except PermissionError as pe:
        print_exception(pe)
        return C.Int(-3)

    if fd is None:
        return C.Int(-1)

    buffer_size = 4096 # Default
    statvfs = None
    block_size = None

    try:
        statvfs = os.statvfs(filename)
        block_size = statvfs.f_bsize
    except:
        block_size = buffer_size

    # allocate memory for buffer
    buf_base = stdlib.malloc(C.size_t(buffer_size))

    # Allocate FILE struct
    file = C.struct(_IO_FILE)
    # set read values first
    file._IO_read_ptr = buf_base
    file._IO_read_end = buf_base # empty buffer at the start
    file._IO_read_base = buf_base

    # set write values
    file._IO_write_base = buf_base
    file._IO_write_ptr = buf_base
    file._IO_write_end = buf_base.ptr_addr + buffer_size

    # set buffer values
    file._IO_buf_base = buf_base
    file._IO_buf_end = buf_base.ptr_addr + buffer_size

    # set file descriptor and block size
    try:
        file._fileno = C.Int(fd.fileno())
    except Exception as e:
        print_exception(e)
        file._fileno = C.Int(-1)

    file._blksize = C.Int(block_size)

    # Store the file descriptor in a global dictionary to keep track of open files
    if "_open_files" not in globals():
        global _open_files
        _open_files = {}
    _open_files[fd.fileno()] = fd

    C.pop_frame()
    return C.pointer(file, C.struct) # Return

def fclose(file_:C.pointer[FILE]) -> C.Int:
    """fclose - Close a file and free its memory

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: 0 on success, -1 on failure"""
    try:
        C.push_frame()
        # Dereference the pointer
        file: C.struct = C.struct.from_address(_IO_FILE, file_.ptr_addr)
        fileno = file._fileno.value

        # Get the file descriptor from the global dictionary
        fd:TextIO = _open_files.get(fileno, None)

        if fd is None:
            return C.Int(-1)

        # Close the file
        fd.close()

        # Free the buffer memory
        stdlib.free(file_) # Free the FILE struct memory
        del file
        del file_

        # Remove the file descriptor from the global dictionary
        del _open_files[fileno]
        C.pop_frame()
        return C.Int(0)
    except Exception as e:
        print_exception(e)
        return C.Int(-1)

def ftell(file: C.pointer[FILE]) -> C.size_t:
    """ftell - Get the current position in the file

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: Current position in the file or -1 on failure"""
    try:
        # Dereference the pointer
        C.push_frame()
        file_struct: C.struct = C.struct.from_address(_IO_FILE, file.ptr_addr)
        fd = _open_files.get(file_struct._fileno.value)
        if not fd:
            del file_struct
            return C.Int(-1)
        out = fd.tell()
        del file_struct
        C.pop_frame()
        return C.size_t(out)
    except Exception as e:
        print_exception(e)
        return C.Int(-1)

def fflush(file: C.pointer[FILE]) -> C.Int:
    """fflush - Flush the output buffer of a file

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: 0 on success, -1 on failure"""
    try:
        # Dereference the pointer
        file_struct: C.struct = C.struct.from_address(_IO_FILE, file.ptr_addr)
        fd:TextIO = _open_files.get(file_struct._fileno.value, None)

        if fd is None:
            return C.Int(-1)

        # Flush the file
        fd.flush()
        del file_struct
        C.pop_frame()
        return C.Int(0)
    except Exception as e:
        print_exception(e)
        return C.Int(-1)

def fseek(file: C.pointer[FILE], offset: C.Int, whence: C.Int) -> C.Int:
    """fseek - Set the file position indicator for the stream

    Arguments:
        file (FILE*):
            Pointer to the FILE struct
        offset (int):
            Offset to set the position to
        whence (int):
            Position from which to set the offset (e.g. SEEK_SET, SEEK_CUR, SEEK_END)

    Returns: 0 on success, -1 on failure"""
    try:
        # Dereference the pointer
        C.push_frame()
        file_struct: C.struct = C.struct.from_address(_IO_FILE, file.ptr_addr)
        fd:TextIO = _open_files.get(file_struct._fileno.value, None)

        if fd is None:
            return Int(-1)

        fd.seek(offset.value, whence.value)
        del file_struct
        C.pop_frame()
        return C.Int(0)
    except Exception as e:
        print_exception(e)
        return C.Int(-1)

def fread(dest: C.pointer[C.void], size: C.size_t, nmemb: C.size_t, file_ptr: C.pointer[FILE]) -> C.Int:
    """fread - Read data from a file

    Args:
        dest (void*): The destination pointer where data will be stored
        size (size_t): size of each element to read
        nmemb (size_t): number of elements to read
        file_ptr (FILE*): Pointer to the FILE struct

    Returns:
        int: Number of elements successfully read, or -1 on failure
    """
    size = size.value
    nmemb = nmemb.value

    try:
        C.push_frame()
        # Dereference the pointer
        file: C.struct = C.struct.from_address(_IO_FILE, file_ptr.ptr_addr)
        total_bytes = size * nmemb

        fileno = file._fileno.value
        fd:TextIO = _open_files.get(fileno, None)
        if fd is None:
            return C.Int(-1)

        data = fd.read(total_bytes)
        if not data:
            return C.Int(0)

        if isinstance(data, str): data = data.encode("utf-8")

        # Write data to the destination pointer
        C.write_mem(data, size.value, dest.ptr_addr)

        # Update the read pointer
        buf_base = file._IO_buf_base
        file._IO_read_ptr = C.pointer(buf_base.ptr_addr + len(data), C.char)
        file._IO_read_end = C.pointer(buf_base.ptr_addr + total_bytes, C.char)

        del file

        C.pop_frame()
        return C.Int(len(data) // size)

    except Exception as e:
        print_exception(e)
        return C.Int(-1)

def fwrite(src: Union[C.pointer[C.void], str, bytes], size: C.size_t, nmemb: C.size_t, file_ptr: C.pointer[FILE], chunk_size:Optional[C.Int]=None) -> C.Int:
    """fwrite - Write data to a file
    
    Args:
        src (void*): The source pointer containing data to write
        size (size_t): size of each element to write
        nmemb (size_t): number of elements to write
        file_ptr (FILE*): Pointer to the FILE struct
        chunk_size (int): Writing files in chunk to prevent overuse of memory. Defaults to 4096 bytes / 4KB

    Returns:
        int: Number of elements successfully written, or -1 on failure
    """
    size = size.value
    nmemb = nmemb.value
    chunk_size = chunk_size.value if chunk_size else 4096

    try:
        C.push_frame()
        # Dereference the pointer
        file:C.struct = C.struct.from_address(_IO_FILE, file_ptr.ptr_addr)
        total_bytes = size * nmemb

        fileno = file._fileno.value
        fd:TextIO = _open_files.get(fileno, None)
        if fd is None:
            return C.Int(-1)
        
        written = 0
        srcaddr = src.ptr_addr
        
        offset = 0
        print("memaddr: ", srcaddr)
        for i in range(nmemb):
            buf = C.read_mem(size, srcaddr + offset)

            fd.write(buf)
            written += 1
            offset += size

        fd.flush()
        os.fsync(fd.fileno())
      
        # Update the write pointer
        buf_base = file._IO_buf_base
        file._IO_write_ptr = C.pointer(buf_base.ptr_addr + written, C.char)

        del file
        
        C.pop_frame()
        return C.Int(written)

    except Exception as e:
        print_exception(e)
        return C.Int(-1)

def remove(filename: Union[C.pointer[C.char], str]) -> C.Int:
    """remove - Remove a file

    Arguments:
        filename (char*):
            Path to the file to remove

    Returns: 0 on success, -1 on failure"""
    try:
        C.push_frame()
        os.remove(_get_string(filename))
        C.pop_frame()
        return C.Int(0)
    except FileNotFoundError as fe:
        print_exception(fe)
        return C.Int(-2)
    except PermissionError as pe:
        print_exception(pe)
        return C.Int(-3)
    except Exception as e:
        print_exception(e)
        return C.Int(-1)

def rename(old_filename: Union[C.pointer[C.char], str], new_filename: Union[C.pointer[C.char], str]) -> C.Int:
    """rename - Rename a file

    Arguments:
        old_filename (char*):
            Path to the file to rename
        new_filename (char*):
            New path for the file

    Returns: 0 on success, -1 on failure"""
    try:
        C.push_frame()
        os.rename(_get_string(old_filename), _get_string(new_filename))
        C.pop_frame()
        return C.Int(0)
    except FileNotFoundError as fe:
        print_exception(fe)
        return C.Int(-2)
    except PermissionError as pe:
        print_exception(pe)
        return C.Int(-3)
    except Exception as e:
        print_exception(e)
        return C.Int(-1)

