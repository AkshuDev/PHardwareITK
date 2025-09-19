"""C-Spectre is a ctypes like library offering auto-resolving, object-oriented, simpler-interface, library-auto-loading, auto-function-resolving and more features while being fully compatible with ctypes"""
import ctypes
import os
import sys
import re

RE_DEFINE   = re.compile(r'^\s*#define\s+(\w+)(?:\s+(.*))?')
RE_UNDEF    = re.compile(r'^\s*#undef\s+(\w+)')
RE_IFDEF    = re.compile(r'^\s*#ifdef\s+(\w+)')
RE_IFNDEF   = re.compile(r'^\s*#ifndef\s+(\w+)')
RE_ELSE     = re.compile(r'^\s*#else')
RE_ENDIF    = re.compile(r'^\s*#endif')
RE_FUNC = re.compile(
    r'^(extern\s+)?'                # extern (optional)
    r'([\w\s\*\_]+?)'               # return type (with * allowed)
    r'\s+(\*?\s*\w+|\(\*\w+\))'     # function name OR (*funcptr)
    r'\s*\((.*?)\)\s*;'             # arguments
)

#macros
NULL = 0x0

#types
class CInt:
    def __init__(self, value:int=0):
        self.value = self._wrap()
        
    def __int__(self):
        return self.value
        
    def __repr__(self):
        return str(self.value)
        
    def _wrap(self, value):
        if self.signed:
            mask = 2**(8*self.size) - 1
            value &= mask
            if value > max_value:
                value -= (mask + 1)
            return value
        else:
            return value & self.max_value
            
    def __add__(self, val:int):
        return type(self)(self.value + int(val))
    
    def __sub__(self, val:int):
        return type(self)(self.value - int(val))
        
    def __mul__(self, val:int):
        return type(self)(self.value * int(val))
        
    def __div__(self, val:int):
        return type(self)(self.value / int(val))
        
    def to_ctypes(self):
        if self.size == 1:
            if self.signed:
                return ctypes.c_int8(self.value)
            else:
                return ctypes.c_uint8(self.value)
        elif self.size == 2:
            if self.signed:
                return ctypes.c_int16(self.value)
            else:
                return ctypes.c_uint16(self.value)
        elif self.size == 4:
            if self.signed:
                return ctypes.c_int32(self.value)
            else:
                return ctypes.c_uint32(self.value)
        elif self.size == 8:
            if self.signed:
                return ctypes.c_int64(self.value)
            else:
                return ctypes.c_uint64(self.value)
        else:
            raise ValueError(f"No such C Type (INT) with size -> {self.size}")
    
class CUint(CInt):
    def __init__(self, value:int):
        self.signed = True
        super().__init__(value)
        
class CUint8(CUint):
    def __init__(self, value:int):
        self.size = 1
        self.min_value = 0x0
        self.max_value = 0xFF
        super().__init__(value)
        
class CUint16(CUint):
    def __init__(self, value:int):
        self.size = 2
        self.min_value = 0x0
        self.max_value = 0xFFFF
        super().__init__(value)
        
class CUint32(CUint):
    def __init__(self, value:int):
        self.size = 4
        self.min_value = 0x0
        self.max_value = 0xFFFFFFFF
        super().__init__(value)
        
class CUint64(CUint):
    def __init__(self, value:int):
        self.size = 8
        self.min_value = 0x0
        self.max_value = 0xFFFFFFFFFFFFFFFF
        super().__init__(value)
        
class CInt8(CInt):
    def __init__(self, value:int):
        self.size = 1
        self.min_value = 0x7F
        self.max_value = 0x80
        super().__init__(value)
        
class CInt16(CInt):
    def __init__(self, value:int):
        self.size = 2
        self.min_value = 0x7FFF
        self.max_value = 0x8000
        super().__init__(value)
        
class CInt32(CInt):
    def __init__(self, value:int):
        self.size = 4
        self.min_value = 0x7FFFFFFF
        self.max_value = 0x80000000
        super().__init__(value)
        
class CInt64(CInt):
    def __init__(self, value:int):
        self.size = 8
        self.min_value = 0x7FFFFFFFFFFFFFFF
        self.max_value = 0x8000000000000000
        super().__init__(value)
        
class Void:
    def __init__(self):
        self.value = None  # always None

    def __repr__(self):
        return "void"

    def to_ctypes(self):
        import ctypes
        return None
        
class Pointer:
    def __init__(self, base_type, value=None):
        self.base_type = base_type
        self.value = value  # can be None initially

    def deref(self):
        if self.value is None:
            raise ValueError("Pointer is NULL")
        return self.value

    def set(self, value):
        if not isinstance(value, self.base_type):
            raise TypeError(f"Expected {self.base_type}, got {type(value)}")
        self.value = value

    def __repr__(self):
        addr = hex(id(self.value)) if self.value is not None else "NULL"
        return f"<Pointer to {self.base_type.__name__} at {addr}>"

    def to_ctypes(self):
        import ctypes
        if self.value is None:
            return ctypes.c_void_p(None)
        elif hasattr(self.value, "to_ctypes"):
            return ctypes.pointer(self.value.to_ctypes())
        else:
            return ctypes.c_void_p(id(self.value))  # fallback
            
class VoidPointer(Pointer):
    def __init__(self, value=None):
        super().__init__(Void, value)

class CPrebuilt:
    def __init__(self):
        self.functions = []
        self.macros = {}
        self.cond_stack = []

    def include(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Header '{path}' not found")
        # Parse header and store metadata for auto-resolve
        content = ""
        with open(path, "r") as f:
            f.seek(0)
            content = f.read()
        
        self.parse(content)
            
    def parse(self, text):
        text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
        for line in text.splitlines():
            #preprocessors
            if m := RE_DEFINE.match(line):
                self.macros[m[1]] = m[2] or "1"
            elif m := RE_UNDEF.match(line):
                self.macros.pop(m[1], None)
            elif m := RE_IFDEF.match(line):
                self.cond_stack.append(m[1])
            elif m := RE_IFNDEF.match(line):
                self.cond_stack.append("!" + m[1])
            elif RE_ELSE.match(line):
                if self.cond_stack:
                    self.cond_stack[-1] = "!" + self.cond_stack[-1]
            elif RE_ENDIF.match(line):
                if self.cond_stack:
                    self.cond_stack.pop()
                    
        #handle funcs
        for func in self.parse_functions(text):
            if not any(f["name"] == func["name"] for f in self.functions):
                self.functions.append(func)
        return {"macros": self.macros, "functions": self.functions}
        
    def _join_function_lines(self, text):
        buf, out = [], []
        for line in text.splitlines():
            buf.append(line.strip())
            if ";" in line:         # function decl ends
                out.append(" ".join(buf))
                buf = []
        return out
        
    def parse_functions(self, text):
        funcs = []
        for stmt in self._join_function_lines(text):
            if m := RE_FUNC.match(stmt):
                raw_return = m[2].strip()
                raw_name   = m[3].strip()
                args       = m[4].strip()

                # Clean up name (handle (*funcptr))
                if raw_name.startswith("(*") and raw_name.endswith(")"):
                    name = raw_name[2:-1]   # strip (* and )
                else:
                    name = raw_name.lstrip("*")

                funcs.append({
                    "extern": bool(m[1]),
                    "return": " ".join(raw_return.split()),  # collapse spaces
                    "name": name,
                    "args": [
                        arg.strip()
                        for arg in args.split(",")
                        if arg.strip() and arg.strip() != "void"
                    ]
                })
        return funcs
            
    def get_function(self, name:str) -> dict:
        return self.functions.get(name, None)

class LibraryWrapper:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Library {path} not found")
        self.path = path
        self._lib = ctypes.CDLL(path)  # ctypes handles platform ABI
        self._func_cache = {} # caches resolved functions

    def __getattr__(self, name):
        # auto-resolve happens here
        if name in self._func_cache:
            return self._func_cache[name]

        try:
            func = getattr(self._lib, name)
        except AttributeError:
            raise AttributeError(f"Function {name} not found in {self.path}")

        # Auto-resolve signature
        func.argtypes, func.restype = self._auto_resolve(name)
        
        def wrapper(*args):
            conv_args = [_to_ctypes(arg) for arg in args]
            res = func(*conv_args)
            return _from_ctypes(res, func.restype)

        self._func_cache[name] = func
        return func
        
    def _auto_resolve(self, func_name):
        return ([], ctypes.c_int)
    
    def _to_ctypes(self, arg):
        if hasattr(arg, "to_ctypes"):
            return arg.to_ctypes()
        else:
            return arg
            
    def _from_ctypes(self, value, restype):
        return value