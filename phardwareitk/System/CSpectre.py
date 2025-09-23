"""C-Spectre is a ctypes like library offering auto-resolving, object-oriented, simpler-interface, library-auto-loading, auto-function-resolving and more features while being fully compatible with ctypes"""
import ctypes
import os
import sys
from typing import *

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
            if value > self.max_value:
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
        self.functions = {}
        self.macros = {}
        self.cond_stack = []
        self.typedefs = {}
        self.enums = {}
        self.structs = {}
        self.inc_dirs = []

    def include(self, path:str, include_dirs: Union[str, list]="", ignore_includes:bool=False):
        """Includes a header file and auto resolves all dependencies, functions, macros and conditionals"""
        if isinstance(include_dirs, str):
            self.inc_dirs.append(include_dirs)
        elif isinstance(include_dirs, list):
            self.inc_dirs = include_dirs
        
        self.inc_dirs.append("")
        exists = False
        
        for dir_ in self.inc_dirs:
            path = os.path.join(dir_, path)
            if os.path.exists(path):
                exists = True
                break
            
        if not exists:
            raise FileNotFoundError(f"Header file {path} was not found!")
        # Parse header and store metadata for auto-resolve
        content = ""
        with open(path, "r") as f:
            f.seek(0)
            content = f.read()

        self.parse(content, ignore_includes)

    def parse(self, text:str, ignore_includes:bool=False):
        """Parse C header text for functions, macros, and conditionals"""
        lines = text.splitlines()
        buffer = []
        in_comment = False
        for line in lines:
            line = line.strip()
            
            if line.endswith("*/") and in_comment:
                in_comment = False
                continue
            
            if in_comment:
                continue
        
            if not line or line.startswith("//"):
                continue  # skip empty lines and single line comments
            
            if line.startswith("/*") and not in_comment:
                in_comment = True
                continue

            # Preprocessor
            if line.startswith("#define"):
                parts = line.split(maxsplit=2)
                key = parts[1]
                val = parts[2] if len(parts) > 2 else "1"
                self.macros[key] = val
                continue
            elif line.startswith("#undef"):
                key = line.split()[1]
                self.macros.pop(key, None)
                continue
            elif line.startswith("#ifdef"):
                self.cond_stack.append(line.split()[1])
                continue
            elif line.startswith("#ifndef"):
                self.cond_stack.append("!" + line.split()[1])
                continue
            elif line.startswith("#else"):
                if self.cond_stack: 
                    self.cond_stack[-1] = "!" + self.cond_stack[-1]
                continue
            elif line.startswith("#endif"):
                if self.cond_stack: 
                    self.cond_stack.pop()
                continue
            elif line.startswith("#include") and not ignore_includes:
                parts = line.split()
                if len(parts) < 2:
                    continue
                file = parts[1].replace('"', "").replace("<", "").replace(">", "")
                self.include(file)

            # Function detection
            buffer.append(line)
            if line.endswith(";") and not line.startswith("typedef"):
                err = self._parse_function(" ".join(buffer))
                if not err == "ERROR":
                    buffer = []
                
            # Typedef/enums/structs
            b1 = buffer[0] if len(buffer) > 0 else ""
            bend = buffer[-1] if len(buffer) > 0 else ""
            if (bend.endswith("}") or bend.endswith(";")) and (b1.startswith("typedef") or (b1.startswith("enum") or b1.startswith("struct"))):
                if b1.startswith("struct"):
                    buffer = []
                    continue
                err = self._parse_tes(" ".join(buffer))
                if not err == "ERROR":
                    buffer = []
            
    def _join_function_lines(self, text:str):
        buf, out = [], []
        for line in text.splitlines():
            buf.append(line.strip())
            if ";" in line:         # function decl ends
                out.append(" ".join(buf))
                buf = []
        return out

    def _parse_function(self, decl:str):
        decl = decl.rstrip(';').strip()
        if '(' not in decl or ')' not in decl:
            return "ERROR"

        # Split into return type, name, args
        ret_and_name, args = decl.split('(', 1)
        
        if not args.startswith(");") and (not args.startswith("void);") and (not args.startswith(")") and not args.startswith("void)"))):
            args = args.rsplit(')', 1)[0]
        else:
            args = "void"
        ret_parts = ret_and_name.strip().split()
        name = ret_parts[-1].lstrip('*')  # handle pointers
        ret_type = " ".join(ret_parts[:-1])
        extern = False
        
        if ret_type.startswith("extern "):
            extern = True
            ret_type = ret_type.replace("extern ", "")
        
        args_list = [a.strip() for a in args.split(',') if a.strip() and a.strip() != "void"]
        
        args_dict = {}
        for item in args_list:
            if not item or item == "void":
                continue
            arg = item.split(" ")
            if len(arg) < 2:
                continue # Skip broken/voids
            args_dict[arg[1]] = arg[0]

        self.functions[name] = {
            "return": ret_type,
            "name": name,
            "args": args_dict,
            "extern": extern,
        }
    
    def _parse_tes(self, text:str) -> None:
        if not text.startswith("typedef") and (not text.startswith("struct") and not text.startswith("enum")):
            return "ERROR"
        
        if text.startswith("typedef"):
            return self._parse_typedef(text)
        if text.startswith("struct"):
            return self._parse_struct(text)
        if text.startswith("enum"):
            return self._parse_enum(text)
            
    def _parse_typedef(self, text:str):
        if not text.startswith("typedef"):
            return "ERROR"
        
        text_arr = text.replace("\n", "").split(" ")
        if len(text_arr) < 3:
            return "ERROR"
        type_ = text_arr[1]
        name = ""
        val = None
        if len(text_arr) > 3:
            if type_ not in ["enum", "struct"]:
                return "ERROR"
            
            if type_ == "enum":
                enum = "".join(text_arr).replace("typedef", "").replace("enum", "")
                if not enum.startswith("{"):
                    return "ERROR"
                
                enum_vals = enum.replace("{", "").split(",")
                if "}" in enum_vals[-1]:
                    final, name = enum_vals[-1].split("}")
                    name = name.replace(";", "")
                    enum_vals[-1] = final
                
                val = enum_vals
        else:
            name = text_arr[2]
            name = name.replace(";", "")
            
        self.typedefs[name] = {
            "name": name,
            "value": val,
            "type": type_
        }

    def get_function(self, name:str) -> dict:
        """Gets a function from the resolved functions"""
        return self.functions.get(name, None)

    @property
    def resolved_macros(self):
        return self.macros

    @property
    def conditional_stack(self):
        return self.cond_stack

    @property
    def resolved_functions(self):
        return self.functions
        
    @property
    def resolved_typedefs(self):
        return self.typedefs
    
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

        def wrapper(self:LibraryWrapper, *args):
            conv_args = [self._to_ctypes(arg) for arg in args]
            res = func(*conv_args)
            return self._from_ctypes(res, func.restype)

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