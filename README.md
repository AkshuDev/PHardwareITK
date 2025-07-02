# PHardwareITK (Pheonix Hardware Interface Toolkit)
[![PyPI Downloads](https://static.pepy.tech/badge/phardwareitk)](https://pepy.tech/projects/phardwareitk)
[![PyPI Downloads](https://static.pepy.tech/badge/phardwareitk/month)](https://pepy.tech/projects/phardwareitk)
[![PyPI Downloads](https://static.pepy.tech/badge/phardwareitk/week)](https://pepy.tech/projects/phardwareitk)
## Overview

PHardwareITK, or Pheonix Hardware Interface Toolkit, is a comprehensive Python module developed by Pheonix Studios (AkshuDev/Akshobhya). This toolkit provides a variety of functions and utilities to assist developers in creating complex command-line applications, graphical user interfaces, system utilities, and more. With over 50 distinct functions and multiple specialized toolsets, PHardwareITK is designed to be versatile, modular, and cross-platform, ensuring compatibility with a wide range of development needs.

For examples please visit -> [https://github.com/AkshuDev/PHardwareITK] and navigate to the Tests folder.

***IMPORTANT NOTE: THIS IS A OUTDATED README, PLEASE USE GITHUB WIKI (READTHEROCS COMMING SOON)***

## Table of Contents ->
1. Module Overview
2. Key Features
3. Installation
4. Usage
5. Available Toolkits
6. Dependencies
7. Contributing
8. License
9. Module Overview

## Details
    
PHardwareITK serves as a complete suite for developing hardware-related applications, system utilities, and GUI-based tools. It aims to provide developers with powerful, efficient, and easy-to-use resources that handle everything from hardware interactions and system monitoring to building sophisticated user interfaces.

The module includes a set of tools for both novice and experienced developers, including:

1. CLI Toolkit: For creating complex command-line applications.
2. GUI Toolkit: A cross-platform framework for building custom graphical applications.
3. ErrorSystem: A comprehensive error handling system.
4. FileSystem: A set of utilities for interacting with various file formats and performing low-level file operations.
5. HGame: A versatile game development framework that supports multiple rendering engines.

## Key Features

1. Cross-Platform: Works on Linux, Windows, and macOS without modification.
2. Modular Design: Includes a variety of specialized toolkits that can be used independently or together.
3. User-Friendly: Functions are designed to be simple to use, but powerful enough for advanced use cases.
4. Customizable: With features like custom error classes and extendable file system operations, users can adapt the toolkit to their specific needs.
5. Comprehensive Documentation: Detailed explanations and examples of how to use each feature.

## Installation
To install PHardwareITK, follow the steps below:

1. Ensure you are using Python 3.7 or later.
2. Install Using the following command

    pip install phardwareitk

3. Or instead download PheonixAppAPI which includes this module pre-installed inside PheonixAppAPI.Apis.Modules.Pre.phardwareitk
4. Install PheonixAppAPI
   
    pip install PheonixAppAPI

5. Navigate to the downloaded PheonixAppAPI folder/Scripts and run PostInstall.py
6. Your good to go

# Usage
Once the module is installed, you can import it into your Python code. Here are some example use cases:

## Example: Using the CLI Toolkit. (Nano Copy in 100 lines)
# Command Line Interface ToolKit Test

    import sys
    import os
    import time
    import keyboard
    import string
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from phardwareitk.CLI import cliToolKit as cli
    from phardwareitk.Extentions import *
    
    global dataBuffer
    dataBuffer:str = ""
    
    def StatusLabel():
        cli.Cursor.MoveCursorToBottom()
        cli.Text.WriteText(" ^X - Exit\t^O - Write Out")
        cli.Cursor.RestoreCursorPosition()
    
    def Start_SuperCLI():
        cli.Screen.ClearScreen()
        cli.Cursor.SetCursorPositionToHome()
        cli.Cursor.SaveCursorPosition()
    
    def WriteOut(data:str):
        cli.Cursor.MoveCursorToBottom()
        cli.Cursor.MoveCursorUp(3)
        cli.Cursor.SetCursorToBeginningOfLine()
        filePath:str = cli.Text.InputText(" File Path: ")
        cli.Screen.ClearCurrentLine()
        cli.Cursor.SetCursorToBeginningOfLine()
        mode:str = cli.Text.InputText(" Mode: ")
        cli.Screen.ClearCurrentLine()
        cli.Cursor.RestoreCursorPosition()
    
        if os.path.exists(filePath):
            cli.Cursor.MoveCursorToBottom()
            cli.Cursor.MoveCursorUp(3)
            cli.Cursor.SetCursorToBeginningOfLine()
            cli.Text.WriteText(" Path Exist!")
            time.sleep(2)
            cli.Screen.ClearCurrentLine()
            cli.Cursor.RestoreCursorPosition()
        else:
            if not mode.lower() in ["binary", "bin", "normal", "utf-8"]:
                cli.Cursor.MoveCursorToBottom()
                cli.Cursor.MoveCursorUp(3)
                cli.Cursor.SetCursorToBeginningOfLine()
                cli.Text.WriteText(" Mode doesn't Exist! Available Modes -> [binary/bin], [normal/utf-8]")
                time.sleep(2)
                cli.Screen.ClearCurrentLine()
                cli.Cursor.RestoreCursorPosition()
            else:
                if mode.lower() == "binary" or mode.lower() == "bin":
                    with open(filePath, "wb") as f:
                        f.write(data.encode())
                        f.close()
                elif mode.lower() == "normal" or mode.lower() == "utf-8":
                    with open(filePath, "w") as f:
                        f.write(data)
                        f.close()
    
        Start_SuperCLI()
        StatusLabel()
    
    def AddData(key:keyboard.KeyboardEvent):
        global dataBuffer
    
        if key.name == "Enter":
            dataBuffer += "\n"
            cli.Text.WriteText("\n")
            cli.Cursor.SaveCursorPosition()
    
        if key.name == "space":
            dataBuffer += " "
            cli.Text.WriteText(" ")
            cli.Cursor.SaveCursorPosition()
    
        if (key.name in string.printable or key.name == "space") and len(key.name) == 1:
            dataBuffer += key.name
            cli.Text.WriteText(key.name)
            cli.Cursor.SaveCursorPosition()
    
    def BackSpace():
        global dataBuffer
        cursor_y, cursor_x = cli.Cursor.CurrentCursorPosition()
    
        if cursor_x > 1:
            dataBuffer = dataBuffer[:-1]
            cli.Text.BackSpaceChar()
    
    def Delete():
        cursor_y, cursor_x = cli.Cursor.CurrentCursorPosition()
    
        if cursor_x <= len(dataBuffer):
            del dataBuffer[cursor_x - 1]
            cli.Text.DeleteChar()
    
    def KeyPress():
        if keyboard.is_pressed("up"):
            cli.Cursor.MoveCursorUp(1)
        elif keyboard.is_pressed("right"):
            cli.Cursor.MoveCursorRight(1)
        elif keyboard.is_pressed("left"):
            cli.Cursor.MoveCursorLeft(1)
        elif keyboard.is_pressed("down"):
            cli.Cursor.MoveCursorDown(1)
        elif keyboard.is_pressed("ctrl+x"):
            cli.Screen.ClearScreen()
            cli.Cursor.SetCursorPositionToHome()
            exit(0)
        elif keyboard.is_pressed("ctrl+o"):
            WriteOut(dataBuffer)
        else:
            key_ = keyboard.read_event()
            if not key_.event_type == keyboard.KEY_UP:
                AddData(key_)
    
    Start_SuperCLI()
    StatusLabel()
    while True:
        KeyPress()

# Available Toolkits ->
1. CLI Toolkit:

The CLI Toolkit provides over 50 distinct functions for creating and managing command-line interfaces (CLI). It enables developers to rapidly build custom CLI applications, similar to nano or other text-based utilities, with minimal lines of code.

Key features:

50+ pre-built functions to handle inputs, outputs, and commands. \
Full control over terminal interactions and interface flow. \
Support for custom command parsing and input handling. \
Text Output/Input with font and colors.

2. GUI Toolkit

The GUI Toolkit is a cross-platform toolkit that allows developers to create complex graphical user interfaces from scratch. It supports multiple UI frameworks including OpenGL, SDL2. The toolkit is fully customizable and provides advanced functionality for creating modern applications.

It is under development and renderGUI.pyx has to be compiled by GCC/Clang and Cython. Instead for the time, use gui_sdl.py (phardwareitk.GUI.gui). The functions inside gui_sdl and renderGUI are supposed to make the process easy, but it is still under development. Hence, you can still use SDL and OpenGL functions to do whatever you want unlike PyQT5 and Tkinter. This toolkit provides all the functions in SDL2 and OpenGL.

Key features:

Full cross-platform support (Linux, Windows, macOS). \
Highly customizable and extensible components. \
Multiple backend support (OpenGL, SDL2).

3. PLTEC

PLTEC (Pheonix Language To Executable Converter) is a separate App that is included with PHardwareITK. You can find the full documentation for PLTEC here -> [https://github.com/AkshuDev/PLTEC].

5. ErrorSystem
   
The ErrorSystem provides a complete error handling framework with over 50 built-in error classes. It also allows users to create custom error classes for more specialized exceptions.

Key features:

A robust set of error classes for different scenarios. \
Custom error class creation for specialized needs. \
Detailed error messages and stack trace support. 

5. System
   
The System folder includes a range of system utilities such as SysUsage, which allows you to monitor and interact with your computer’s hardware and devices.

Key features:

50+ functions to interact with hardware, monitor system performance, and manage processes. \
Real-time usage statistics and logging.

6. Extensions
   
The Extensions folder provides enhanced versions of Python's built-in functions, adding more capabilities. For example, the printH function in the HyperOut.py file allows for advanced text printing with background and foreground colors, fonts, and other enhancements. It also includes custom functions that make hard parts of programming easy like -> progressH that can create a progress bar in the terminal. It is highly flexible.

NOTE: Mostly all terminal tasks even inside the phardwareitk are done using the cliToolKit.py (phardwareitk.CLI.cliToolKit).

NOTE: phardwareitk.Extensions.HyperIn.inputH is a fully custom input function that doesn't use Python's input. Hence, some important factors are to NOTE -

a. It is still Under Enhancements and if any bug occurs please provide a detailed explanation in [https://github/AkshuDev/PHardwareITK/Issues].
b. It requires a time sleep to prevent CPU Hogging, the cpuHogging parameter in the function is defined to be 0.005 seconds or 5 milliseconds, you cannot go under 3 milliseconds or 0.003 seconds, as it is very dangerous for the CPU to do so.

Key features:

Extended versions of basic Python functions. \
Support for custom styling (colors, fonts) in terminal output. \
Enhanced file writing operations. 

7. FileSystem
   
The FileSystem toolkit provides utilities for performing file operations, including working with JSON, assembly, and binary formats. The module includes over 50 functions for tasks ranging from simple file manipulation to complex data transformations.

Key features:

Support for JSON, binary, and assembly file formats. \
High-level functions for file manipulation and data storage.

8. HGame
   
HGame is an alternative to Pygame, providing a more flexible framework for game development. It supports multiple rendering backends, including PHardwareITK.GUI, Tkinter, OpenGL, and SDL2, making it highly cross-platform.

NOTE: Not yet ready for use, just use GUI toolkit for the time.

Key features:

Multiple rendering backends. \
Cross-platform game development support. \
Easy-to-use game object management and event handling.

9. Dependencies.py
    
The Dependencies.py file contains a list of all required libraries and modules for PHardwareITK. This file ensures that any missing dependencies are noted and can be easily installed. NOTE: All requirements are default modules. This files Exisits to install them incase, they are deleted.

11. LIB.py
    
The LIB.py file contains a class called Paths, which provides access to file paths across the entire module. This class is useful for dynamically managing file locations without hardcoding paths.

# Dependencies

PHardwareITK is designed to run with mostly the Python standard library, ensuring compatibility across all systems with minimal need for external dependencies. However, in the case that any of the pre-installed modules are deleted or missing, the Dependencies.py file will help ensure that all necessary libraries are present.

Required Dependencies ->

1. PySDL2 (pip install pysdl2)
2. PySDL2-DLL (pip install pysdl2-dll)
3. PyOpenGL (pip install PyOpenGL)

NOTE: All these are for the gui toolkit.

# Contributing

We welcome contributions from the community! If you have ideas for new features, bug fixes, or improvements, please follow the steps below:

# Fork the repository.

Create a new branch (git checkout -b feature-branch).\
Make your changes. \
Commit your changes (git commit -m 'Add new feature'). \
Push to your branch (git push origin feature-branch). \
Open a pull request with a description of your changes. 

# License

PHardwareITK is licensed under the MIT License. Feel free to use, modify, and distribute the software under the terms of this license.

# For more information, refer to the official documentation or reach out to us through the repository issues page.
