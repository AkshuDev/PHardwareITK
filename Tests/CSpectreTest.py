import os
import sys

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if not path in sys.path:
    sys.path.append(path)

from phardwareitk.System.CSpectre import *

# Including a header
lib = LibraryWrapper
preblt = CPrebuilt()

preblt.include(input("Header file: "))
print("Functions")
print(preblt.resolved_functions)
print("Macros")
print(preblt.resolved_macros)
print("Conditional Stack")
print(preblt.conditional_stack)