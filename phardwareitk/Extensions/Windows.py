"""This file includes everything you can think of for making C/Python/Asm/C++/C#/etc code for windows, which will run on any OS that python runs on."""

import sys
from . import *

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk.Extensions.C import *

from typing import *

# Winuser.h -> Class Styles
CS_BYTEALIGNCLIENT = 0x1000
CS_BYTEALIGNWINDOW = 0x2000
CS_CLASSDC = 0x0040
CS_DBLCLKS = 0x0008
CS_DROPSHADOW = 0x00020000
CS_GLOBALCLASS = 0x4000
CS_HREDRAW = 0x0002
CS_NOCLOSE = 0x0200
CS_OWNDC = 0x0020
CS_PARENTDC = 0x0080
CS_SAVEBITS = 0x0800
CS_VREDRAW = 0x0001

# winuser.h -> Icons
IDI_APPLICATION = 32512
IDI_ERROR = 32513
IDI_QUESTION = 32514
IDI_WARNING = 32515
IDI_INFORMATION = 32516
IDI_WINLOGO = 32517
IDI_SHIELD = 32518

# winuser.h -> Cursors
IDC_ARROW = 32512
IDC_IBEAM = 32513
IDC_WAIT = 32514
IDC_CROSS = 32515
IDC_UPARROW = 32516
IDC_SIZENWSE = 32642
IDC_SIZENESW = 32643
IDC_SIZEWE = 32644
IDC_SIZENS = 32645
IDC_SIZEALL = 32646
IDC_NO = 32648
IDC_HAND = 32649
IDC_APPSTARTING = 32650
IDC_HELP = 32651
IDC_PIN = 32671
IDC_PERSON = 32672

# wingdi -> GetStockObject
# These are copied from win32con (only these ones not others)
WHITE_BRUSH = 0
LTGRAY_BRUSH = 1
GRAY_BRUSH = 2
DKGRAY_BRUSH = 3
BLACK_BRUSH = 4
NULL_BRUSH = 5
HOLLOW_BRUSH = NULL_BRUSH
WHITE_PEN = 6
BLACK_PEN = 7
NULL_PEN = 8
OEM_FIXED_FONT = 10
ANSI_FIXED_FONT = 11
ANSI_VAR_FONT = 12
SYSTEM_FONT = 13
DEVICE_DEFAULT_FONT = 14
DEFAULT_PALETTE = 15

# winuser.h -> Size and location
CW_USEDEFAULT = -2147483648

# winuser.h -> Show Window
SW_HIDE = 0
SW_SHOWNORMAL = 1
SW_NORMAL = 1
SW_SHOWMINIMIZED = 2
SW_SHOWMAXIMIZED = 3
SW_MAXIMIZED = 3
SW_SHOWNOACTIVATE = 4
SW_SHOW = 5
SW_MINIMIZE = 6
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA = 8
SW_RESTORE = 9
SW_SHOWDEFAULT = 10
SW_FORCEMINIMIZE = 11

# wingdi -> Painting and Drawing Messages
WM_DISPLAYCHANGE = 126
WM_ERASEBKGND = 20
WM_NCPAINT = 133
WM_PAINT = 15
WM_PRINT = 791
WM_PRINTCLIENT = 792
WM_SETREDRAW = 11
WM_SYNCPAINT = 136
# Windows Message Exit
WM_DESTROY = 2

# winuser.h -> PeekMessage Constants Part-1
PM_NOREMOVE = 0x0000
PM_REMOVE = 0x0001
PM_NOYIELD = 0x0002

# Basic Classes and typedefs

class LPCWSTR(str):
    """Represents a pointer to a wide-character string (Unicode)."""

class DWORD(int):
    """Represents a 32-bit unsigned integer."""

class HANDLE(int):
    """Represents a handle to an object (file, process, etc.)."""
    INVALID_HANDLE_VALUE = -1  # Represents a failure case

class BOOL(int):
    """Represents a bool.
    """

class BYTE(int):
  """Represents a byte."""
  pass

class WORD(int):
  """Represents a word (16-bit unsigned integer)"""
  pass

class LONG(int):
    """Represents a LONG (32-bit signed integer)."""
    pass

class PLONG(Pointer):
    """Represents a pointer to a LONG (32-bit signed integer)."""

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("PLONG must point to an int.")
        super().__init__()

class LPVOID(Pointer):
    """A Pointer to a void type."""

    def __init__(self, value: bytearray):
        if not isinstance(value, (bytes, bytearray)):
            raise TypeError("LPVOID must point to bytes or bytearray.")
        super().__init__(value)

class LPCVOID(Pointer):
    """A Pointer to a constant void type (immutable raw bytes)."""

    def __init__(self, value: bytes):
        if not isinstance(value, bytes):
            raise TypeError("LPCVOID must point to immutable bytes.")
        super().__init__(value)

class LPDWORD(Pointer):
    """A Pointer to a DWORD (32-bit unsigned integer)."""

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("LPDWORD must point to an int.")
        super().__init__(value)

class LPLONG(Pointer):
    """A Pointer to a LONG (32-bit signed integer)."""

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("LPLONG must point to an int.")
        super().__init__(value)

class LPOVERLAPPED(Pointer):
    """A Pointer to an OVERLAPPED structure."""

    def __init__(self, value: dict):
        if not isinstance(value, dict):
            raise TypeError("LPOVERLAPPED must point to a dictionary.")
        super().__init__(value)

class LPSECURITY_ATTRIBUTES(Pointer):
    """A Pointer to security attributes."""

    def __init__(self, value: dict):
        if not isinstance(value, dict):
            raise TypeError("LPSECURITY_ATTRIBUTES must point to a dictionary.")
        super().__init__(value)

class LPCVOID(Pointer):
    """A Pointer to a constant void type (immutable raw bytes)."""

    def __init__(self, value: bytes):
        if not isinstance(value, bytes):
            raise TypeError("LPCVOID must point to immutable bytes.")
        super().__init__(value)

# File System and IO
# fileapi, winioctl, ioapiset, namedpipeapi, pipe

class FileAccessMode:
    """A class for all the File Access modes, example -> read, write, etc
    """
    READ = 0x80000000
    WRITE = 0x40000000
    EXECUTE = 0x20000000
    ALL = 0x10000000

    @staticmethod
    def convert_to_python(value: Union[int, DWORD]) -> str:
        """
        Converts a DWORD value to a Python file mode string (e.g., "r", "w", "w+", "a+").
        """
        if not isinstance(value, int):
            return ""

        read = bool(value & FileAccessMode.GENERIC_READ)
        write = bool(value & FileAccessMode.GENERIC_WRITE)
        execute = bool(value & FileAccessMode.GENERIC_EXECUTE)
        all_access = bool(value & FileAccessMode.GENERIC_ALL)

        if all_access:
            return "r+b"  # Example of all access. Adjust if necessary.

        if read and write:
            return "r+" if not execute else "r+b"  # Binary if execute is true.
        if read:
            return "r" if not execute else "rb"  # Binary if execute is true.
        if write:
            return "w" if not execute else "wb"  # Binary if execute is true.
        if execute:
            return "x"  # or "xb". Adjust as needed.

        return ""

class FileDisposition:
    """Defines Windows file creation/opening behaviors."""

    CREATE_NEW = 1
    CREATE_ALWAYS = 2
    OPEN_EXISTING = 3
    OPEN_ALWAYS = 4
    TRUNCATE_EXISTING = 5

class FilePointerMoveMethod:
    """Defines how file pointers are moved."""

    FILE_BEGIN = 0
    FILE_CURRENT = 1
    FILE_END = 2

class FileHandleManager:
    """Manages file handles."""

    _handle_counter = 4  # Windows starts at small non-zero values.
    _open_files: Dict[int, IO] = {}

    @classmethod
    def create_handle(cls, file_path: str, mode: str) -> HANDLE:
        """Creates and registers a file handle."""
        try:
            file_obj = open(file_path, mode)
            handle_id = cls._handle_counter
            cls._open_files[handle_id] = file_obj
            cls._handle_counter += 1
            return HANDLE(handle_id)
        except IOError:
            return HANDLE(HANDLE.INVALID_HANDLE_VALUE)

    @classmethod
    def get_file(cls, handle: HANDLE) -> Optional[IO]:
        """Retrieves a file object from a handle."""
        return cls._open_files.get(handle)

    @classmethod
    def close_handle(cls, handle: HANDLE) -> BOOL:
        """Closes a handle and removes it from tracking."""
        file_obj = cls._open_files.pop(handle, None)
        if file_obj:
            file_obj.close()
            return BOOL(True)
        return BOOL(False)

class FILE_TYPE:
    """File types returned by GetFileType"""
    UNKNOWN = 0x0000
    DISK = 0x0001
    CHAR = 0x0002
    PIPE = 0x0003

class FILE_INFO:
    """Represents file information returned by GetFileInformationByHandle."""
    def __init__(self, file_size: DWORD, creation_time: DWORD, last_access_time: DWORD, last_write_time: DWORD):
        self.file_size = file_size
        self.creation_time = creation_time
        self.last_access_time = last_access_time
        self.last_write_time = last_write_time

class FileAttributes:
    """Represents file attribute flags used in Windows API."""

    READONLY = 0x00000001
    HIDDEN = 0x00000002
    SYSTEM = 0x00000004
    DIRECTORY = 0x00000010
    ARCHIVE = 0x00000020
    DEVICE = 0x00000040
    NORMAL = 0x00000080
    TEMPORARY = 0x00000100
    SPARSE_FILE = 0x00000200
    REPARSE_POINT = 0x00000400
    COMPRESSED = 0x00000800
    OFFLINE = 0x00001000
    NOT_CONTENT_INDEXED = 0x00002000
    ENCRYPTED = 0x00004000

class FileAPI:
    @staticmethod
    def CreateFileW(lpFileName:LPCWSTR, dwDesiredAccess:Union[FileAccessMode, DWORD], dwShareMode:DWORD, lpSecurityAttributes:LPSECURITY_ATTRIBUTES, dwCreationDisposition:DWORD, dwFlagsAndAttributes:DWORD, hTemplateFile:HANDLE) -> HANDLE:
        """
        Opens or creates a file, device, pipe, or other system object.

        Parameters:
            lpFileName (LPCWSTR): The name of the file or device to be created/opened.
            dwDesiredAccess (FileAccessMode | DWORD): The requested access (read, write, execute).
            dwShareMode (DWORD): The sharing mode (e.g., read/write sharing).
            lpSecurityAttributes (Optional[LPSECURITY_ATTRIBUTES]): Security attributes for the file.
            dwCreationDisposition (DWORD): Action to take if the file exists or not (CREATE_NEW, OPEN_EXISTING, etc.).
            dwFlagsAndAttributes (DWORD): File attributes and flags (e.g., FILE_ATTRIBUTE_NORMAL).
            hTemplateFile (HANDLE): Handle to a template file (if applicable).

        Returns:
            HANDLE: A handle to the created or opened file. INVALID_HANDLE_VALUE (-1) on failure.
        """
        mode = {
            FileDisposition.CREATE_NEW: "x",
            FileDisposition.CREATE_ALWAYS: "w",
            FileDisposition.OPEN_EXISTING: "r",
            FileDisposition.OPEN_ALWAYS: "a+",
            FileDisposition.TRUNCATE_EXISTING: "w"
        }.get(dwCreationDisposition, "r")

        # Convert Windows FileAccess flags into Python file modes
        if dwDesiredAccess & FileAccessMode.GENERIC_WRITE:
            mode += "+"
        elif dwDesiredAccess & FileAccessMode.GENERIC_READ:
            mode = "r"

        return FileHandleManager.create_handle(lpFileName, mode)

    @staticmethod
    def CloseHandle(hObject:HANDLE) -> BOOL:
        """Closes a handle."""
        return FileHandleManager.close_handle(hObject)

    @staticmethod
    def ReadFile(hFile: HANDLE, lpBuffer: LPVOID, nNumberOfBytesToRead: DWORD, lpNumberOfBytesRead: LPDWORD, lpOverlapped: LPOVERLAPPED) -> BOOL:
        """
        Reads data from the specified file.

        Parameters:
            hFile (HANDLE): Handle to the file.
            lpBuffer (LPVOID): Buffer to receive data.
            nNumberOfBytesToRead (DWORD): Maximum number of bytes to read.
            lpNumberOfBytesRead (LPDWORD): Pointer to variable that receives the number of bytes read.
            lpOverlapped (LPOVERLAPPED): Pointer to an OVERLAPPED structure (for async I/O, not implemented).

        Returns:
            BOOL: True if successful, False otherwise.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return BOOL(False)

        try:
            data = file.read(nNumberOfBytesToRead)
            lpBuffer[:len(data)] = data.encode()  # Store data in lpBuffer
            lpNumberOfBytesRead.value = len(data)  # Store bytes read
            return BOOL(True)
        except Exception:
            return BOOL(False)

    @staticmethod
    def WriteFile(hFile: HANDLE, lpBuffer: LPCVOID, nNumberOfBytesToWrite: DWORD, lpNumberOfBytesWritten: LPDWORD, lpOverlapped: LPOVERLAPPED) -> BOOL:
        """
        Writes data to the specified file.

        Parameters:
            hFile (HANDLE): Handle to the file.
            lpBuffer (LPCVOID): The data to write.
            nNumberOfBytesToWrite (DWORD): Number of bytes to write.
            lpNumberOfBytesWritten (LPDWORD): Pointer to variable that receives the number of bytes written.
            lpOverlapped (LPOVERLAPPED): Pointer to an OVERLAPPED structure (for async I/O, not implemented).

        Returns:
            BOOL: True if successful, False otherwise.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return BOOL(False)

        try:
            written = file.write(lpBuffer[:nNumberOfBytesToWrite].decode())  # Write bytes
            file.flush()  # Ensure data is saved
            lpNumberOfBytesWritten.value = written  # Store bytes written
            return BOOL(True)
        except Exception:
            return BOOL(False)

    @staticmethod
    def SetFilePointer(hFile: HANDLE, lDistanceToMove: LONG, lpDistanceToMoveHigh: PLONG, dwMoveMethod: DWORD) -> DWORD:
        """
        Moves the file pointer of an open file.

        Parameters:
            hFile (HANDLE): Handle to the file.
            lDistanceToMove (LONG): Number of bytes to move.
            lpDistanceToMoveHigh (PLONG): Pointer to high-order bytes of move distance (not used in this implementation).
            dwMoveMethod (DWORD): Move method (beginning, current, or end).

        Returns:
            DWORD: The new file pointer position, or -1 on failure.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return DWORD(-1)

        try:
            import os
            if dwMoveMethod == FilePointerMoveMethod.FILE_BEGIN:
                file.seek(lDistanceToMove, os.SEEK_SET)
            elif dwMoveMethod == FilePointerMoveMethod.FILE_CURRENT:
                file.seek(lDistanceToMove, os.SEEK_CUR)
            elif dwMoveMethod == FilePointerMoveMethod.FILE_END:
                file.seek(lDistanceToMove, os.SEEK_END)

            return DWORD(file.tell())  # Return new file pointer position
        except Exception:
            return DWORD(-1)

    @staticmethod
    def GetFileSize(hFile:HANDLE, lpFileSizeHigh:LPDWORD) -> DWORD:
        """
        Retrieves the size of a specified file.

        Parameters:
            hFile (HANDLE): Handle to the file whose size is being queried.
            lpFileSizeHigh (LPDWORD): Pointer to a variable that receives the high-order DWORD of the file size.

        Returns:
            DWORD: The low-order part of the file size. Returns INVALID_FILE_SIZE (-1) on failure.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return DWORD(-1)  # INVALID_FILE_SIZE

        try:
            import os
            current_pos = file.tell()  # Save current position
            file.seek(0, os.SEEK_END)
            size = file.tell()
            file.seek(current_pos, os.SEEK_SET)  # Restore file position

            if lpFileSizeHigh is not None:
                lpFileSizeHigh.value = (size >> 32) & 0xFFFFFFFF  # Set high-order 32 bits

            return DWORD(size & 0xFFFFFFFF)  # Return low-order 32 bits
        except Exception:
            return DWORD(-1)

    @staticmethod
    def FlushFileBuffers(hFile: HANDLE) -> BOOL:
        """
        Flushes buffers of the specified file, ensuring data is written to disk.

        Parameters:
            hFile (HANDLE): Handle to the file.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return BOOL(False)

        try:
            file.flush()
            return BOOL(True)
        except Exception:
            return BOOL(False)

    @staticmethod
    def SetEndOfFile(hFile: HANDLE) -> BOOL:
        """
        Truncates or extends a file to the current file pointer position.

        Parameters:
            hFile (HANDLE): Handle to the file.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return BOOL(False)

        try:
            file.truncate()
            return BOOL(True)
        except Exception:
            return BOOL(False)

    @staticmethod
    def GetFileInformationByHandle(hFile: HANDLE) -> Optional[FILE_INFO]:
        """
        Retrieves file metadata.

        Parameters:
            hFile (HANDLE): Handle to the file.

        Returns:
            Optional[FILE_INFO]: File metadata if successful, otherwise None.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return None

        try:
            import os

            stats = os.stat(file.fileno())
            return FILE_INFO(
                file_size=DWORD(stats.st_size),
                creation_time=DWORD(int(stats.st_ctime)),
                last_access_time=DWORD(int(stats.st_atime)),
                last_write_time=DWORD(int(stats.st_mtime)),
            )
        except Exception:
            return None

    @staticmethod
    def GetFileType(hFile: HANDLE) -> DWORD:
        """
        Retrieves the type of file (disk, char, or pipe).

        Parameters:
            hFile (HANDLE): Handle to the file.

        Returns:
            DWORD: File type.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return DWORD(FILE_TYPE.UNKNOWN)

        if file.isatty():
            return DWORD(FILE_TYPE.CHAR)
        return DWORD(FILE_TYPE.DISK)

    @staticmethod
    def DuplicateHandle(hSourceHandle: HANDLE) -> HANDLE:
        """
        Duplicates an existing handle.

        Parameters:
            hSourceHandle (HANDLE): Handle to duplicate.

        Returns:
            HANDLE: A new handle if successful, INVALID_HANDLE_VALUE (-1) otherwise.
        """
        file = FileHandleManager.get_file(hSourceHandle)
        if not file:
            return HANDLE(HANDLE.INVALID_HANDLE_VALUE)

        try:
            new_handle = FileHandleManager.create_handle(file.name, file.mode)
            return new_handle
        except Exception:
            return HANDLE(HANDLE.INVALID_HANDLE_VALUE)

    @staticmethod
    def LockFile(hFile: HANDLE, dwFileOffsetLow: DWORD, dwFileOffsetHigh: DWORD, nNumberOfBytesToLock: DWORD) -> BOOL:
        """
        Locks a region of a file.

        Parameters:
            hFile (HANDLE): Handle to the file.
            dwFileOffsetLow (DWORD): Low-order part of the starting byte offset.
            dwFileOffsetHigh (DWORD): High-order part of the starting byte offset.
            nNumberOfBytesToLock (DWORD): Number of bytes to lock.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return BOOL(False)

        # Simulating a lock (Python does not have direct lock API)
        return BOOL(True)

    @staticmethod
    def UnlockFile(hFile: HANDLE, dwFileOffsetLow: DWORD, dwFileOffsetHigh: DWORD, nNumberOfBytesToUnlock: DWORD) -> BOOL:
        """
        Unlocks a previously locked region.

        Parameters:
            hFile (HANDLE): Handle to the file.
            dwFileOffsetLow (DWORD): Low-order part of the starting byte offset.
            dwFileOffsetHigh (DWORD): High-order part of the starting byte offset.
            nNumberOfBytesToUnlock (DWORD): Number of bytes to unlock.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        file = FileHandleManager.get_file(hFile)
        if not file:
            return BOOL(False)

        # Simulating unlock (Python does not have direct unlock API)
        return BOOL(True)

    @staticmethod
    def LockFileEx(hFile: HANDLE, dwFlags: DWORD, dwReserved: DWORD, nNumberOfBytesToLockLow: DWORD, nNumberOfBytesToLockHigh: DWORD, lpOverlapped: LPOVERLAPPED) -> BOOL:
        """
        Locks a region of a file with additional options.

        Parameters:
            hFile (HANDLE): Handle to the file.
            dwFlags (DWORD): Locking flags.
            dwReserved (DWORD): Reserved, must be zero.
            nNumberOfBytesToLockLow (DWORD): Low-order part of the lock range.
            nNumberOfBytesToLockHigh (DWORD): High-order part of the lock range.
            lpOverlapped (LPOVERLAPPED): Overlapped structure.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        return FileAPI.LockFile(hFile, nNumberOfBytesToLockLow, nNumberOfBytesToLockHigh, 0)

    @staticmethod
    def UnlockFileEx(hFile: HANDLE, dwReserved: DWORD, nNumberOfBytesToUnlockLow: DWORD, nNumberOfBytesToUnlockHigh: DWORD, lpOverlapped: LPOVERLAPPED) -> BOOL:
        """
        Unlocks a previously locked region (extended).

        Parameters:
            hFile (HANDLE): Handle to the file.
            dwReserved (DWORD): Reserved, must be zero.
            nNumberOfBytesToUnlockLow (DWORD): Low-order part of the unlock range.
            nNumberOfBytesToUnlockHigh (DWORD): High-order part of the unlock range.
            lpOverlapped (LPOVERLAPPED): Overlapped structure.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        return FileAPI.UnlockFile(hFile, nNumberOfBytesToUnlockLow, nNumberOfBytesToUnlockHigh, 0)

    @staticmethod
    def DeleteFileW(lpFileName:LPCWSTR) -> BOOL:
        """
        Deletes a File.

        Parameters:
            lpFileName (LPCWSTR): The name of the file to be deleted.

        Returns:
            BOOL: True if successfull, else False
        """

        import os

        if not os.path.exists(lpFileName):
            return BOOL(False)

        try:
            os.remove(lpFileName)
            return BOOL(True)
        except Exception:
            return BOOL(False)

    @staticmethod
    def GetFileAttributesW(lpFileName:LPCWSTR) -> DWORD:
        """Gets the file Attributes

        Args:
            lpFileName (LPCWSTR): The name of the file or directory.

        Returns:
            DWORD: If the function succeeds, the return value contains the attributes of the specified file or directory, If the function fails, the return value is **INVALID_FILE_ATTRIBUTES**.
        """
        import os
        import stat

        if not os.path.exists(lpFileName):
            return DWORD(-1)

        try:
            attributes = 0

            #Assign attribs
            if os.path.isdir(lpFileName):
                attributes |= FileAttributes.DIRECTORY
            if os.path.isfile(lpFileName):
                attributes |= FileAttributes.NORMAL
            if not os.access(lpFileName, os.W_OK):
                attributes |= FileAttributes.READONLY
            if os.stat(lpFileName).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN:
                attributes |= FileAttributes.HIDDEN

            return DWORD(attributes)
        except Exception:
            return DWORD(-1)

    @staticmethod
    def SetFileAttributesW(lpFileName:LPCWSTR, dwFileAttributes: DWORD) -> BOOL:
        """
        Sets attributes for the specified file.

        Parameters:
            lpFileName (LPCWSTR): The name of the file.
            dwFileAttributes (DWORD): The new file attributes to be set.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        import os
        import stat

        if not os.path.exists(lpFileName):
            return BOOL(False)

        try:
            # Remove READONLY FLAG, if needed
            if dwFileAttributes & FileAttributes.READONLY:
                os.chmod(lpFileName, stat.S_IREAD)
            else:
                os.chmod(lpFileName, stat.S_IWRITE)

            # Handle hidden attribute (cross-platform)
            file_dir, file_name = os.path.split(lpFileName)
            new_file_name = f".{file_name}" if dwFileAttributes & FileAttributes.HIDDEN and not file_name.startswith(".") else file_name
            new_file_path = os.path.join(file_dir, new_file_name)

            # Rename only if necessary
            if new_file_path != lpFileName:
                os.rename(lpFileName, new_file_path)

            return BOOL(True)

            return BOOL(True)
        except Exception:
            return BOOL(False)

    @staticmethod
    def GetFileTime(hFile: HANDLE, lpCreationTime:LPDWORD, lpLastAccessTime:LPDWORD, lpLastWriteTime: LPDWORD) -> BOOL:
        """
        Retrieves the creation, last access, and last write times of a file.

        Parameters:
            hFile (HANDLE): Handle to the file.
            lpCreationTime (LPDWORD): Pointer to store creation time.
            lpLastAccessTime (LPDWORD): Pointer to store last access time.
            lpLastWriteTime (LPDWORD): Pointer to store last write time.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        import os
        import time

        file = FileHandleManager.get_file(hFile)
        if not file:
            return BOOL(False)

        try:
            stats = os.stat(file.name)
            lpCreationTime.value = DWORD(int(stats.st_birthtime))
            lpLastAccessTime.value = DWORD(int(stats.st_atime))
            lpLastWriteTime.value = DWORD(int(stats.st_mtime))
            return BOOL(True)
        except Exception:
            return BOOL(False)

    @staticmethod
    def SetFileTime(hFile: HANDLE, lpCreationTime: LPDWORD, lpLastAccessTime: LPDWORD, lpLastWriteTime: LPDWORD) -> BOOL:
        """
        Sets the creation, last access, and last write times of a file.

        Parameters:
            hFile (HANDLE): Handle to the file.
            lpCreationTime (LPDWORD): Pointer to new creation time.
            lpLastAccessTime (LPDWORD): Pointer to new last access time.
            lpLastWriteTime (LPDWORD): Pointer to new last write time.

        Returns:
            BOOL: True if successful, False otherwise.
        """
        import os
        import time

        file = FileHandleManager.get_file(hFile)
        if not file:
            return BOOL(False)

        try:
            times = (
                lpLastAccessTime.value if lpLastAccessTime else None,
                lpLastWriteTime.value if lpLastWriteTime else None,
            )
            os.utime(file.name, times)
            return BOOL(True)
        except Exception:
            return BOOL(False)

