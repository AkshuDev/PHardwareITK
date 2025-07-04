from typing import *
import os
import sys
import time

if not os.path.dirname(os.path.abspath(__file__)) in sys.path:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from C import *


_IO_FILE = {
    "_IO_read_ptr": {
        "type": Pointer[Char],
        "value": None
    },
    "_IO_read_end": {
        "type": Pointer[Char],
        "value": None
    },
    "_IO_read_base": {
        "type": Pointer[Char],
        "value": None
    },
    "_IO_write_base": {
        "type": Pointer[Char],
        "value": None
    },
    "_IO_write_ptr": {
        "type": Pointer[Char],
        "value": None
    },
    "_IO_write_end": {
        "type": Pointer[Char],
        "value": None
    },
    "_IO_buf_base": {
        "type": Pointer[Char],
        "value": None
    },
    "_IO_buf_end": {
        "type": Pointer[Char],
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

FILE = Struct[_IO_FILE]

def fopen(path:Pointer[Char], mode:Pointer[Char]) -> Union[Pointer[FILE], int]:
    """fopen - Open a file and return a FILE struct pointer

    Arguments:
        path (char*):
            Path to the file
        mode (char*):
            Mode to open the file with (e.g. 'r', 'w', 'rb', ...)

    Returns: Pointer to FILE (_IO_FILE) struct or -1 on failure, -2 on file not found, -3 on permission error"""
    filename = get_string(path)
    mode = get_string(mode)

    fd = None

    try:
        fd = open(filename, mode)
    except PermissionError:
        return -3

    if fd is None:
        return -1

    buffer_size = 4096 # Default
    statvfs = None
    block_size = None

    try:
        statvfs = os.statvfs(filename)
        block_size = statvfs.f_bsize
    except:
        block_size = buffer_size

    # allocate memory for buffer
    buf_base = malloc(buffer_size)

    # Allocate FILE struct
    file = FILE(_IO_FILE)
    # set read values first
    file.set("_IO_read_ptr", buf_base)
    file.set("_IO_read_end", buf_base) # empty buffer at the start
    file.set("_IO_read_base", buf_base)

    # set write values
    file.set("_IO_write_base", buf_base)
    file.set("_IO_write_ptr", buf_base)
    file.set("_IO_write_end", buf_base.address + buffer_size)

    # set buffer values
    file.set("_IO_buf_base", buf_base)
    file.set("_IO_buf_end", buf_base.address + buffer_size)

    # set file descriptor and block size
    try:
        file.set("_fileno", fd.fileno())
    except Exception as e:
        file.set("_fileno", -1)

    file.set("_blksize", block_size)

    # Store the file descriptor in a global dictionary to keep track of open files
    if "_open_files" not in globals():
        global _open_files
        _open_files = {}
    _open_files[file.access("_fileno")] = fd

    return Pointer(Struct, file, True) # Return

def fclose(file_:Pointer[FILE]) -> int:
    """fclose - Close a file and free its memory

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: 0 on success, -1 on failure"""
    try:
        # Dereference the pointer
        file: Struct = file_.dereference()
        fileno = file.access("_fileno")

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

        return 0
    except Exception as e:
        return -1

def ftell(file: Pointer[FILE]) -> int:
    """ftell - Get the current position in the file

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: Current position in the file or -1 on failure"""
    try:
        # Dereference the pointer
        file_struct: Struct = file.dereference()
        out = file_struct.access("_IO_read_ptr") - file_struct.access("_IO_read_base")
        del file_struct
        return out
    except Exception as e:
        return -1

def fflush(file: Pointer[FILE]) -> int:
    """fflush - Flush the output buffer of a file

    Arguments:
        file (FILE*):
            Pointer to the FILE struct

    Returns: 0 on success, -1 on failure"""
    try:
        # Dereference the pointer
        file_struct: Struct = file.dereference()
        fd:TextIO = _open_files.get(file_struct.access("_fileno"), None)

        if fd is None:
            return -1

        # Flush the file
        fd.flush()
        del file_struct
        return 0
    except Exception as e:
        return -1

def fseek(file: Pointer[FILE], offset: int, whence: int) -> int:
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
        file_struct: Struct = file.dereference()
        fd:TextIO = _open_files.get(file_struct.access("_fileno"), None)

        if fd is None:
            return -1

        fd.seek(offset, whence)
        del file_struct
        return 0
    except Exception as e:
        return -1

def fread(dest: Pointer[Void], size: Union[int, Size_t], nmemb: Union[int, Size_t], file_ptr: Pointer[FILE]) -> int:
    """fread - Read data from a file

    Args:
        dest (Pointer[Void]): The destination pointer where data will be stored
        size (int): size of each element to read
        nmemb (int): number of elements to read
        file_ptr (Pointer[FILE]): Pointer to the FILE struct

    Returns:
        int: Number of elements successfully read, or -1 on failure
    """
    if isinstance(size, Size_t):
        size = size.bytes

    if isinstance(nmemb, Size_t):
        nmemb = nmemb.bytes

    if not isinstance(size, int) or not isinstance(nmemb, int):
        raise TypeError("size and nmemb must be int or Size_t")

    try:
        # Dereference the pointer
        file:FILE = file_ptr.dereference()
        total_bytes = size * nmemb

        fileno = file.access("_fileno")
        fd:TextIO = _open_files.get(fileno, None)
        if fd is None:
            return -1

        data = fd.read(total_bytes)
        if not data:
            return 0

        # Write data to the destination pointer
        write(dest, data, total_bytes)

        # Update the read pointer
        buf_base = file.access("_IO_buf_base")
        file.set("_IO_read_ptr", Pointer(buf_base.address + len(data)))
        file.set("_IO_read_end", Pointer(buf_base.address + total_bytes))

        del file

        return len(data) // size

    except Exception as e:
        return -1

def fwrite(src: Pointer[Void], size: Union[int, Size_t], nmemb: Union[int, Size_t], file_ptr: Pointer[FILE]) -> int:
    """fwrite - Write data to a file

    Args:
        src (Pointer[Void]): The source pointer containing data to write
        size (int): size of each element to write
        nmemb (int): number of elements to write
        file_ptr (Pointer[FILE]): Pointer to the FILE struct

    Returns:
        int: Number of elements successfully written, or -1 on failure
    """
    if isinstance(size, Size_t):
        size = size.bytes

    if isinstance(nmemb, Size_t):
        nmemb = nmemb.bytes

    if not isinstance(size, int) or not isinstance(nmemb, int):
        raise TypeError("size and nmemb must be int or Size_t")

    try:
        # Dereference the pointer
        file:FILE = file_ptr.dereference()
        total_bytes = size * nmemb

        fileno = file.access("_fileno")
        fd:TextIO = _open_files.get(fileno, None)
        if fd is None:
            return -1

        # Read data from the source pointer
        data = read(src, total_bytes)

        if not 'b' in fd.mode:
            try:
                data = data.decode('utf-8')
            except UnicodeDecodeError:
                return -1

        # Write data to the file
        fd.write(data)

        # Update the write pointer
        buf_base = file.access("_IO_buf_base")
        file.set("_IO_write_ptr", Pointer(buf_base.address + len(data)))

        del file

        return len(data) // size

    except Exception as e:
        return -1

def remove(filename: Pointer[Char]) -> int:
    """remove - Remove a file

    Arguments:
        filename (char*):
            Path to the file to remove

    Returns: 0 on success, -1 on failure"""
    try:
        os.remove(get_string(filename))
        return 0
    except FileNotFoundError:
        return -2
    except PermissionError:
        return -3
    except Exception as e:
        return -1

def rename(old_filename: Pointer[Char], new_filename: Pointer[Char]) -> int:
    """rename - Rename a file

    Arguments:
        old_filename (char*):
            Path to the file to rename
        new_filename (char*):
            New path for the file

    Returns: 0 on success, -1 on failure"""
    try:
        os.rename(get_string(old_filename), get_string(new_filename))
        return 0
    except FileNotFoundError:
        return -2
    except PermissionError:
        return -3
    except Exception as e:
        return -1

