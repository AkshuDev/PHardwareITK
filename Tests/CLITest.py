# Command Line Interface ToolKit Test

import sys
import os
import time
import keyboard
import string

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from phardwareitk.CLI import cliToolKit as cli
from phardwareitk.Extensions import *

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

    if (key.name in string.printable or key.name == "space") and (len(key.name) == 1 or len(key.name == 5)):
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