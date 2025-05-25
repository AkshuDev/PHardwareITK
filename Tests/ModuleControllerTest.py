import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from phardwareitk.ModuleController import main

print("v0001 compiler")
compiler = main.Compiler()

compiler.set("he", "hello")
compiler.set("llo", "world")
compiler.saveToFile(True)
time.sleep(2)
compiler.getFromFile()
print(compiler.decompile_v0001())
print(compiler.get("llo"))

print("v0001 compiler [no encrypt]")
compilerOptions = main.CompilerOptions(encrypt=False)
compiler = main.Compiler(compilerOptions=compilerOptions)

compiler.set("he", "hello")
compiler.set("llo", "world")
compiler.saveToFile(True)
time.sleep(2)
compiler.getFromFile()
print(compiler.decompile_v0001())
print(compiler.get("llo"))

print("v0002 compiler")
compilerOptions = main.CompilerOptions(encrypt=True, format_="COMPILER_pheonix$phardwareitk$v0002")
compiler = main.Compiler(compilerOptions=compilerOptions)

compiler.set("he", "hello")
compiler.set("llo", "world")
compiler.saveToFile(True)
time.sleep(2)
compiler.getFromFile()
print(compiler.decompile_v0002())
print(compiler.get("llo"))

print("v0002 compiler [no encrypt]")
compilerOptions = main.CompilerOptions(encrypt=False, format_="COMPILER_pheonix$phardwareitk$v0002")
compiler = main.Compiler(compilerOptions=compilerOptions)

compiler.set("he", "hello")
compiler.set("llo", "world")
compiler.saveToFile(True)
time.sleep(2)
compiler.getFromFile()
print(compiler.decompile_v0002())
print(compiler.get("llo"))