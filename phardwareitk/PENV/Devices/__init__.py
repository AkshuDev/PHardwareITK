from . import console
from . import keyboard

CONSOLE0 = console.ConsoleDevice()
KEYBOARD_PS2_0 = keyboard.KeyboardPs2Device()

def route_devices(port: int, arg: int, inout: bool): # inout = True (os used __in__), False (os used __out__)
    if port < 0x0:
        return
    
    if port in [0x1, 0x2, 0x3]:
        return console.console_route(CONSOLE0, port, arg, inout)
    if port in [0x60, 0x64]:
        return keyboard.keyboard_ps2_route(KEYBOARD_PS2_0, port, arg, inout)
    if inout:
        return 0
        
def route_in(port: int):
    return route_devices(port, None, True)
    
def route_out(port: int, arg: int):
    route_devices(port, arg, False)
    return None
    
def setup():
    KEYBOARD_PS2_0.setup()
    
def end():
    KEYBOARD_PS2_0.deinit()