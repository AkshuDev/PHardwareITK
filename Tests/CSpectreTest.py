import os
import sys

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if path not in sys.path:
    sys.path.append(path)

from phardwareitk.System.CSpectre import LibraryWrapper, CPrebuilt

# Including a header
lib = LibraryWrapper
preblt = CPrebuilt()
useDef = input("Use default (y/n) (default is y): ").lower()
def_ = False
if useDef not in ["y", "n", "yes", "no", "yup", "nope", "nah", ""]:
    raise ValueError("y/n/Nothing Only")
elif useDef in ["y", "yes", "yup", ""]:
    def_ = True
IncludeDir = input("Include Directory (leave for None): ") if def_ is False else "Tests"
file = input("Header File: ") if def_ is False else "CSpectreTest.h"
do_includes = input("Allow includes (y/n) (default is yes): ").lower()
includes = False
if do_includes not in ["y", "yes", "yup", "", "true", "n", "no", "nope", "nah", "false"]:
    raise ValueError("y/n/Nothing Only!")
elif do_includes in ["n", "no", "nope", "nah", "false"]:
    includes = True

preblt.include(file, IncludeDir, includes)
print("Functions")
print(preblt.resolved_functions)
print("Macros")
print(preblt.resolved_macros)
print("Conditional Stack")
print(preblt.conditional_stack)
print("Typedefs")
print(preblt.resolved_typedefs)