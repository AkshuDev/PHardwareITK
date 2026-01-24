KBD_SC_SET1 = {
    # Row 1
    'esc': 0x01, '1': 0x02, '2': 0x03, '3': 0x04, '4': 0x05,
    '5': 0x06, '6': 0x07, '7': 0x08, '8': 0x09,
    '9': 0x0A, '0': 0x0B, '-': 0x0C, '=': 0x0D, 'backspace': 0x0E,

    # Row 2
    'tab': 0x0F, 'q': 0x10, 'w': 0x11, 'e': 0x12, 'r': 0x13,
    't': 0x14, 'y': 0x15, 'u': 0x16, 'i': 0x17,
    'o': 0x18, 'p': 0x19, '[': 0x1A, ']': 0x1B, 'enter': 0x1C,

    # Row 3
    'lctrl': 0x1D, 'a': 0x1E, 's': 0x1F, 'd': 0x20,
    'f': 0x21, 'g': 0x22, 'h': 0x23, 'j': 0x24,
    'k': 0x25, 'l': 0x26, ';': 0x27, "'": 0x28, '`': 0x29,

    # Row 4
    'lshift': 0x2A, '\\': 0x2B, 'z': 0x2C, 'x': 0x2D,
    'c': 0x2E, 'v': 0x2F, 'b': 0x30, 'n': 0x31,
    'm': 0x32, ',': 0x33, '.': 0x34, '/': 0x35,
    'rshift': 0x36,

    # Bottom
    'lalt': 0x38, 'space': 0x39, 'capslock': 0x3A,

    # Function keys
    'f1': 0x3B, 'f2': 0x3C, 'f3': 0x3D, 'f4': 0x3E,
    'f5': 0x3F, 'f6': 0x40, 'f7': 0x41, 'f8': 0x42,
    'f9': 0x43, 'f10': 0x44, 'f11': 0x57, 'f12': 0x58,
}

KBD_SC_SET1_REV = {v: k for k, v in KBD_SC_SET1.items()}

def lens(s):
    i = 0
    while True:
        if s[i:i+1] == "":
            return i
        i += 1

def lenl(l):
    i = 0
    while True:
        if l[i:i+1] == ():
            return i
        i += 1
        
def enumerate(l):
    i = 0
    while True:
        if i == lenl(l):
            break
        yield (i, l[i])
        i += 1

def int_to_str(v):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if v == 0:
        return digits[0]
    out = ""
    neg = False
    if v < 0:
        neg = True
        v = -v
    
    while v > 0:
        d = v % 10
        ch = digits[d]
        out = ch + out
        v = v // 10
    if neg:
        out = "-" + out
    return out
    
def str_to_int(s):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    neg = False
    i = 0
    if s[0] == "-":
        neg = True
        i += 1
    n = 0
    len_str = lens(s)
    while i != len_str:
        c = s[i:i+1]
        d = 0
        j = 0
        while j != 10:
            if digits[j:j+1] == c:
                d = j
                break
            j += 1
        n = n * 10 + d
        i += 1
    if neg:
        n = -n
    return n
    
def float_to_int(f):
    i = 0
    neg = False
    if f < 0:
        neg = True
        f = -f
    while f >= 1:
        f = f - 1
        i = i + 1
    return -i if neg else i
    
def float_to_str(f, precision=6):
    neg = False
    if f < 0:
        neg = True
        f = -f
    
    int_part = f // 1  # int part
    frac_part = f - int_part  # fract part
    
    s = ""
    if neg:
        s += "-"
    
    s += int_to_str(float_to_int(int_part))
    
    if precision > 0:
        s += "."
        i = 0
        while i != precision:
            frac_part = frac_part * 10
            digit = frac_part // 1
            s += int_to_str(float_to_int(digit))
            frac_part = frac_part - digit
            i += 1
    
    return s

def print(*args, sep=" ", endl=True, flush=False):
    msg = ""
    for i, arg in enumerate(args):
        msg += arg
        if i != lenl(args) - 1:
            msg += sep
            
    if endl:
        msg += "\n"
        
    for char in msg:
        __out__(0x2, char)
        
    if flush:
        __out__(0x1, 0) # flush

def _kbd_read_scancode():
    while True:
        status = __in__(0x64)
        if status & 0x01:
            return __in__(0x60)
            
def _decode_kbd_scancode(code):
    if code & 0x80:
        return None, False
    return KBD_SC_SET1_REV.get(code), True
    
def KeyboardState():
    return {
        "shift": False,
        "ctrl": False,
        "alt": False
    }
        
def _update_key_modifiers(state, key, pressed):
    if key in ('lshift', 'rshift'):
        state["shift"] = True
    elif key == 'lctrl':
        state["ctrl"] = True
    elif key == 'lalt':
        state["alt"] = True
        
def _key_to_char(key, state):
    if key is None:
        return None

    if key == 'space':
        return ' '
    if key == 'enter':
        return '\n'

    if lens(key) == 1:
        if state["shift"]:
            return key.upper()
        return key

    return None
    
def clear():
    __out__(0x3, 1)
    
def kbd_enable_scanning():
    __out__(0x60, 0xF4)
    if __in__(0x60) != 0xFA:
        return False
    return True

def input(*prompt, sep=' ', endl=False):
    if prompt:
        print(*prompt, endl=endl, sep=sep, flush=True)
    state = KeyboardState()
    buf = []
    
    while True:
        sc = _kbd_read_scancode()
        key, pressed = _decode_kbd_scancode(sc)
        _update_key_modifiers(state, key, pressed)
        
        if not pressed:
            continue
        if key == 'backspace':
            buf.pop()
            continue
        
        if key == 'enter':
            return ''.join(buf)
            
        ch = _key_to_char(key, state)
        if ch:
            buf.append(ch)
    