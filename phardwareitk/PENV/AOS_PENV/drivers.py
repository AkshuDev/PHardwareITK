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
        __out__(0x2, str_to_int(char))
        
    if flush:
        __out__(0x1, 0) # flush
