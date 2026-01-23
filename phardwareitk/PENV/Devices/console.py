class ConsoleDevice:
    def __init__(self):
        self.buffer = ""
    
    def cmd_console_flush(self, val: int, inout: bool):
        print(self.buffer, end='', sep='', flush=True)
        self.buffer = ""
        if inout:
            return 1
            
    def cmd_console_write(self, val: int, inout: bool):
        self.buffer += str(val)
        if inout:
            return 1
    
def console_route(console: ConsoleDevice, port:int, arg: int, inout: bool):
    if port == 0x1:
        return console.cmd_console_flush(arg, inout)
    elif port == 0x2:
        return console.cmd_console_write(arg, inout)
    if inout:
        return 0