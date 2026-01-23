from . import console

CONSOLE0 = console.ConsoleDevice()

def route_devices(port: int, arg: int, inout: bool): # inout = True (os used __in__), False (os used __out__)
    if port < 0x0:
        return
    
    if port <= 0x4:
        return console.console_route(CONSOLE0, port, arg, inout)
    if inout:
        return 0
        
def route_in(port: int, arg: int):
    return route_devices(port, arg, True)
    
def route_out(port: int, arg: int):
    route_devices(port, arg, False)
    return None