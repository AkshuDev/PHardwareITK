import threading
import time
import sys

SC_SET1 = {
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

SC_SET2 = {
    # Row 1
    'esc': 0x76, '1': 0x16, '2': 0x1E, '3': 0x26, '4': 0x25,
    '5': 0x2E, '6': 0x36, '7': 0x3D, '8': 0x3E,
    '9': 0x46, '0': 0x45, '-': 0x4E, '=': 0x55,
    'backspace': 0x66,

    # Row 2
    'tab': 0x0D, 'q': 0x15, 'w': 0x1D, 'e': 0x24,
    'r': 0x2D, 't': 0x2C, 'y': 0x35, 'u': 0x3C,
    'i': 0x43, 'o': 0x44, 'p': 0x4D,
    '[': 0x54, ']': 0x5B, 'enter': 0x5A,

    # Row 3
    'lctrl': 0x14, 'a': 0x1C, 's': 0x1B, 'd': 0x23,
    'f': 0x2B, 'g': 0x34, 'h': 0x33, 'j': 0x3B,
    'k': 0x42, 'l': 0x4B, ';': 0x4C,
    "'": 0x52, '`': 0x0E,

    # Row 4
    'lshift': 0x12, '\\': 0x5D, 'z': 0x1A, 'x': 0x22,
    'c': 0x21, 'v': 0x2A, 'b': 0x32, 'n': 0x31,
    'm': 0x3A, ',': 0x41, '.': 0x49, '/': 0x4A,
    'rshift': 0x59,

    # Bottom
    'lalt': 0x11, 'space': 0x29, 'capslock': 0x58,

    # Function keys
    'f1': 0x05, 'f2': 0x06, 'f3': 0x04, 'f4': 0x0C,
    'f5': 0x03, 'f6': 0x0B, 'f7': 0x83, 'f8': 0x0A,
    'f9': 0x01, 'f10': 0x09, 'f11': 0x78, 'f12': 0x07,
}

class KeyboardPs2Device:
    def __init__(self):
        self.scanning = False
        self.leds = 0
        self.nxt_cmd = 0x0
        self.repeat_rate = 0
        self.sc_set = 1
        
        self._running = False
        self.thread = None
        
        self.queue = []
        self.status_reg = 0
        
    def enq(self, val):
        self.queue.append(val & 0xFF)
        self.status_reg |= 0x01
        
    def read_status(self):
        return self.status_reg
        
    def read_data(self):
        if not self.queue:
            self.status_reg &= ~0x01
            return 0
        v = self.queue.pop(0)
        if not self.queue:
            self.status_reg &= ~ 0x01
        return v
        
    def enable_scanning(self):
        self.scanning = True
        return 0xFA
    
    def disable_scanning(self):
        self.scanning = False
        return 0xFA
        
    def reset(self):
        self.scanning = False
        self.sc_set = 1
        self.leds = 0
        self.repeat_rate = 0
        self.status_reg = 0
        self.queue = []
        self.enq(0xFA)
        return 0xAA
    
    def set_leds(self, arg):
        self.leds = arg
        return 0xFA
    
    def set_typematic(self, arg):
        self.repeat_rate = arg
        return 0xFA
    
    def identity(self):
        self.enq(0xFA)
        self.enq(0xAB)
        return 0x83
    
    def set_scancode_set(self, arg):
        self.sc_set = arg
        return 0xFA
        
    def route_x60(self, arg):
        if self.nxt_cmd == 0x0:
            if arg in (0xF4, 0xF5, 0xF2, 0xFF):
                if arg == 0xF4:
                    self.enq(self.enable_scanning())
                elif arg == 0xF5:
                    self.enq(self.disable_scanning())
                elif arg == 0xFF:
                    self.enq(self.reset())
                elif arg == 0xF2:
                    self.enq(self.identity())
            else:
                if arg in (0xED, 0xF3, 0xF0):
                    self.nxt_cmd = arg
                    self.enq(0xFA)
                else:
                    self.enq(0xFE)
            return None
        cmd = self.nxt_cmd
        self.nxt_cmd = 0
        if cmd == 0xED:
            self.enq(self.set_leds(arg))
        elif cmd == 0xF3:
            self.enq(self.set_typematic(arg))
        elif cmd == 0xF0:
            self.enq(self.set_scancode_set(arg))
        else:
            self.enq(0xFE)
            
    def setup(self):
        self._running = True
        def worker():
            while self._running:
                ev = self._scan_key()
                if ev is not None:
                    self._push_key(ev, True)
                    self._push_key(ev, False)
                time.sleep(0.001) # 1KHz polling
                
        self.thread = threading.Thread(target=worker, daemon=True)
        self.thread.start()
        
    def deinit(self):
        self._running = False
        self.thread.join()
    
    def _push_key(self, key, pressed):
        if not self.scanning:
            return
        
        if self.sc_set == 1:
            code = SC_SET1.get(key, None)
            if not code:
                return None
            if pressed:
                self.enq(code)
            else:
                self.enq(code | 0x80)
        elif self.sc_set == 2:
            code = SC_SET2.get(key, None)
            if not code:
                return None
            if pressed:
                self.enq(0x80)
            self.enq(code)
            
    def _scan_key(self):
        ch = sys.stdin.read(1)
        if ch == ' ':
            ch = 'space'
        elif ch == '\n':
            ch = 'enter'
        elif ch == '\b' or ch == '\x7f':
            ch = 'backspace'
        return ch.lower()
            
def keyboard_ps2_route(keyboard: KeyboardPs2Device, port: int, arg: int, inout: bool):
    if port == 0x60 and inout:
        return keyboard.read_data()
    elif port == 0x64 and inout:
        return keyboard.read_status()
    elif port == 0x60 and not inout:
        return keyboard.route_x60(arg)