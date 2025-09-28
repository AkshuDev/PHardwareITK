import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.PENV import *

os = input("Install a OS? (leave for not installing anything, else give path to the folder): ")
format_ = input("Format Disk? (y/N): ").lower()
if format_ == "y":
    format_ = True
else:
    format_ = False

start_penv(command_py="py", os=os, format_drive=format_)