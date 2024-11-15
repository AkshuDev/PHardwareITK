pyCode = """helloWorld = "Hi"
helloWorldBuffer = 'H'
helloWB = True
hiiiiiiiii = 0
hellll = 0.1
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.Extensions.HyperPython import *

Convert(0, pyCode)