import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.Extensions.C import *

if __name__ == "__main__":
    print("Creating a char")
    char = Char('H')
    print(char)
    print("Creating a Pointer to [char]")
    pointer = Pointer(char.value)
    print(pointer)
    print("Creating a short")
    short = Short(char.value)
    print(short)
    print("Defining [Char, Int, Short] of types as Signed")
    signedC = Signed(char)
    signedI = Signed(char.value)
    signedS = Signed(short)
    print(signedC)
    print(signedI)
    print(signedS)