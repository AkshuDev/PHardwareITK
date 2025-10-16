from typing import *
import os
import sys

from phardwareitk.Extensions.C import *
from phardwareitk.Extensions.C.stdlib import *

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
        "type": pointer,
        "ptr_type": char,
        "value": None
    },
    "_IO_read_end": {
        "type": pointer,
        "ptr_type": char,
        "value": None
    },
    "_IO_read_base": {
        "type": pointer,
        "ptr_type": char,
        "value": None
    },
    "_IO_write_base": {
        "type": pointer,
        "ptr_type": char,
        "value": None
    },
    "_IO_write_ptr": {
        "type": pointer,
        "ptr_type": char,
        "value": None
    },
    "_IO_write_end": {
        "type": pointer,
        "ptr_type": char,
        "value": None
    },
    "_IO_buf_base": {
        "type": pointer,
        "ptr_type": char,
        "value": None
    },
    "_IO_buf_end": {
        "type": pointer,
        "ptr_type": char,
        "value": None
    },
    "_fileno": {
        "type": Int,
        "value": None
    },
    "_blksize": {
        "type": Int,
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

FILE = struct[_IO_FILE]

def _get_string(ptr: Union[pointer[char], str, None]) -> str:
    if ptr is None: return None
    if isinstance(ptr, str): return ptr
    return ptr.deref()

def fopen(path:Union[pointer[char], str], mode:Union[pointer[char], str]) -> Union[pointer[FILE], Int]:
    """fopen - Open a file and return a FILE struct pointer

    Arguments:
        path (char*):
            Path to the file
        mode (char*):
            Mode to open the file with (e.g. 'r', 'w', 'rb', ...)

    Returns: Pointer to FILE (_IO_FILE) struct or -1 on failure, -2 on file not found, -3 on permission error"""
    push_frame()
    filename = _get_string(path)
    mode = _get_string(mode)

    fd = None

    try:
        fd = open(filename, mode)
    except PermissionError as pe:
        print_exception(pe)
        return Int(-3)

    if fd is None:
        return Int(-1)

    buffer_size = 4096 # Default
    statvfs = None
    block_size = None

    try:
        statvfs = os.statvfs(filename)
        block_size = statvfs.f_bsize
    except:
        block_size = buffer_size

    # allocate memory for buffer
    buf_base = malloc(size_t(buffer_size))

    # Allocate FILE struct
    file = struct(_IO_FILE)
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
        file._fileno = Int(fd.fileno())
    except Exception as e:
        print_exception(e)
        file._fileno = Int(-1)

    file._blksize = Int(block_size)

    # Store the file descriptor in a global dictionary to keep track of open files
    if "_open_files" not in globals():
        global _open_files
        _open_files = {}
    _open_files[fd.fileno()] = fd

    pop_frame()
    return pointer(file, struct) # Return

def fclose(file_:pointer[FILE]) -> Int:
    """fclose - Close a file and free its memory

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: 0 on success, -1 on failure"""
    try:
        push_frame()
        # Dereference the pointer
        file: struct = struct.from_address(_IO_FILE, file_.ptr_addr)
        fileno = file._fileno.value

        # Get the file descriptor from the global dictionary
        fd:TextIO = _open_files.get(fileno, None)

        if fd is None:
            return -1

        # Close the file
        fd.close()

        # Free the buffer memory
        free(file_) # Free the FILE struct memory
        del file
        del file_

        # Remove the file descriptor from the global dictionary
        del _open_files[fileno]
        pop_frame()
        return Int(0)
    except Exception as e:
        print_exception(e)
        return Int(-1)

def ftell(file: pointer[FILE]) -> size_t:
    """ftell - Get the current position in the file

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: Current position in the file or -1 on failure"""
    try:
        # Dereference the pointer
        push_frame()
        file_struct: struct = struct.from_address(_IO_FILE, file.ptr_addr)
        fd = _open_files.get(file_struct._fileno.value)
        if not fd:
            del file_struct
            return -1
        out = fd.tell()
        del file_struct
        pop_frame()
        return size_t(out)
    except Exception as e:
        print_exception(e)
        return Int(-1)

def fflush(file: pointer[FILE]) -> Int:
    """fflush - Flush the output buffer of a file

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: 0 on success, -1 on failure"""
    try:
        # Dereference the pointer
        file_struct: struct = struct.from_address(_IO_FILE, file.ptr_addr)
        fd:TextIO = _open_files.get(file_struct._fileno.value, None)

        if fd is None:
            return Int(-1)

        # Flush the file
        fd.flush()
        del file_struct
        pop_frame()
        return Int(0)
    except Exception as e:
        print_exception(e)
        return Int(-1)

def fseek(file: pointer[FILE], offset: Int, whence: Int) -> Int:
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
        push_frame()
        file_struct: struct = struct.from_address(_IO_FILE, file.ptr_addr)
        fd:TextIO = _open_files.get(file_struct._fileno.value, None)

        if fd is None:
            return Int(-1)

        fd.seek(offset.value, whence.value)
        del file_struct
        pop_frame()
        return Int(0)
    except Exception as e:
        print_exception(e)
        return Int(-1)

def fread(dest: pointer[void], size: size_t, nmemb: size_t, file_ptr: pointer[FILE]) -> Int:
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
        push_frame()
        # Dereference the pointer
        file: struct = struct.from_address(_IO_FILE, file_ptr.ptr_addr)
        total_bytes = size * nmemb

        fileno = file._fileno.value
        fd:TextIO = _open_files.get(fileno, None)
        if fd is None:
            return Int(-1)

        data = fd.read(total_bytes)
        if not data:
            return Int(0)

        if isinstance(data, str): data = data.encode("utf-8")

        # Write data to the destination pointer
        write_mem(data, size.value, dest.ptr_addr)

        # Update the read pointer
        buf_base = file._IO_buf_base
        file._IO_read_ptr = pointer(buf_base.ptr_addr + len(data), char)
        file._IO_read_end = pointer(buf_base.ptr_addr + total_bytes, char)

        del file

        pop_frame()
        return Int(len(data) // size)

    except Exception as e:
        print_exception(e)
        return Int(-1)

def fwrite(src: Union[pointer[void], str, bytes], size: size_t, nmemb: size_t, file_ptr: pointer[FILE], chunk_size:Optional[Int]=None) -> Int:
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
        push_frame()
        # Dereference the pointer
        file:struct = struct.from_address(_IO_FILE, file_ptr.ptr_addr)
        total_bytes = size * nmemb

        fileno = file._fileno.value
        fd:TextIO = _open_files.get(fileno, None)
        if fd is None:
            return Int(-1)
        
        written = 0
        srcaddr = src.ptr_addr
        
        offset = 0
        for i in range(nmemb):
            buf = read_mem(size, srcaddr + offset)
            if not 'b' in fd.mode:
                try:
                    buf = buf.decode("utf-8")
                except UnicodeDecodeError:
                    return Int(-1)

            fd.write(buf)
            written += 1
            offset += size
      
        # Update the write pointer
        buf_base = file._IO_buf_base
        file._IO_write_ptr = pointer(buf_base.ptr_addr + written, char)

        del file
        
        pop_frame()
        return Int(written)

    except Exception as e:
        print_exception(e)
        return Int(-1)

def remove(filename: Union[pointer[char], str]) -> Int:
    """remove - Remove a file

    Arguments:
        filename (char*):
            Path to the file to remove

    Returns: 0 on success, -1 on failure"""
    try:
        push_frame()
        os.remove(_get_string(filename))
        pop_frame()
        return Int(0)
    except FileNotFoundError as fe:
        print_exception(fe)
        return Int(-2)
    except PermissionError as pe:
        print_exception(pe)
        return Int(-3)
    except Exception as e:
        print_exception(e)
        return Int(-1)

def rename(old_filename: Union[pointer[char], str], new_filename: Union[pointer[char], str]) -> Int:
    """rename - Rename a file

    Arguments:
        old_filename (char*):
            Path to the file to rename
        new_filename (char*):
            New path for the file

    Returns: 0 on success, -1 on failure"""
    try:
        push_frame()
        os.rename(_get_string(old_filename), _get_string(new_filename))
        pop_frame()
        return Int(0)
    except FileNotFoundError as fe:
        print_exception(fe)
        return Int(-2)
    except PermissionError as pe:
        print_exception(pe)
        return Int(-3)
    except Exception as e:
        print_exception(e)
        return Int(-1)

