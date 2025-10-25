"""Hardware Hyper Game (HGame).

To Use, pass parameters in **HGame_Settings**. Also no need to save it, as it has a automated system, to provide all functions with every parameter needed. Check file for code. And then the stage is yours!
"""

import os
import sys
import platform

PHardwareITK = len(sys.path) - 1
PHardwareITK_P = os.path.join(os.path.dirname(__file__), "..", "..")

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk.Extensions import *
from phardwareitk.Extensions import HyperOut as HOut

class HGame_OUT:
    """This class defined **Output** locations available for HGame.
    """
    @staticmethod
    def console() -> int:
        return 0

    @staticmethod
    def stdout() -> int:
        return HGame_OUT.console()

    @staticmethod
    def messagebox() -> int:
        return 2

    @staticmethod
    def file() -> int:
        return 4

    if platform.platform().lower() == "windows":
        def winEventManager() -> int:
            return 3

class HGame_Settings:
    """This class offers the settings for using HGame.

    Parameters:
        output [HGame_OUT]: Defined where errors and logs will be displayed. Defaults to **HGame_OUT.stdout**
        debug [bool]: If true, Debug mode will be used. Defaults to False.
        filesystem_encrypt [bool]: If true, Creation of files via HGame_FileManager will be encrypted. Defaults to False.
    """
    _instances:list = []

    def __init__(self, output:HGame_OUT=HGame_OUT.stdout, debug:bool=False, filesystem_encrypt:bool=False) -> None:
        if not isinstance(output, HGame_OUT):
            HOut.printH("[HGAME ERROR] ->\n\tArgument [output] takes a [HGame_OUT] class only.", FontEnabled=True, Font=TextFont(font_color=Color("red")))
            raise TypeError("See Above for ERROR.")
        if not isinstance(debug, bool):
            HOut.printH("[HGAME ERROR] ->\n\tArgument [debug] takes a [bool] class only.", FontEnabled=True, Font=TextFont(font_color=Color("red")))
            raise TypeError("See Above for ERROR.")
        if not isinstance(filesystem_encrypt, bool):
            HOut.printH("[HGAME ERROR] ->\n\tArgument [filesystem_encrypt] takes a [bool] class only.", FontEnabled=True, Font=TextFont(font_color=Color("red")))
            raise TypeError("See Above for ERROR.")

        self.output:int = output()
        self.debug:bool = debug
        self.filesystem_encrypt:bool = filesystem_encrypt

        if not HGame_Settings._instances:
            HGame_Settings._instances.append(self)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HGame_Settings, cls).__new__(cls)
            cls._instance.initialize_values() # call the initialization function
        return cls._instance

    @property
    def output_(self) -> int:
        return self.output

    @property
    def debug_(self) -> bool:
        return self.debug

    @property
    def filesystem_encrypt_(self) -> bool:
        return self.filesystem_encrypt

    @classmethod
    def get_first_instance(cls):
        if cls._instances:
            return cls._instances[0]
        else:
            return None

    def __str__(self) -> str:
        return f"Hyper Game Settings"

    def __repr__(self) -> str:
        return f"Hyper Game Settings ->\n\tOutput: {self.output}\n\tDebug: {self.debug}\n\tFile Encrypt: {self.filesystem_encrypt}"

from phardwareitk.GUI import gui

# phardwareitk/HGame/core.py

class GameObject:
    """
    Represents an entity within the game world.

    Attributes:
        name (str): The name of the GameObject.
        position (tuple): The (x, y) coordinates of the GameObject.
        components (list): A list of Component objects attached to the GameObject.
    """

    def __init__(self, name="GameObject", position=(0, 0)):
        """
        Initializes a new GameObject.

        Args:
            name (str, optional): The name of the GameObject. Defaults to "GameObject".
            position (tuple, optional): The (x, y) coordinates. Defaults to (0, 0).
        """
        self.name = name
        self.position = position
        self.components = []

    def add_component(self, component):
        """
        Adds a Component to the GameObject.

        Args:
            component (Component): The Component object to add.
        """
        self.components.append(component)
        component.game_object = self

    def get_component(self, component_type):
        """
        Retrieves a Component of a specific type.

        Args:
            component_type (type): The type of Component to retrieve.

        Returns:
            Component or None: The Component object if found, otherwise None.
        """
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

class Component:
    """
    Base class for components that can be attached to GameObjects.

    Attributes:
        game_object (GameObject or None): The GameObject this Component is attached to.
    """

    def __init__(self):
        """
        Initializes a new Component.
        """
        self.game_object = None

class Sprite(Component):
    """
    Represents a visual sprite for a GameObject.

    Attributes:
        image (str): The path to the image file.
    """

    def __init__(self, image):
        """
        Initializes a new Sprite.

        Args:
            image (str): The path to the image file.
        """
        super().__init__()
        self.image = image

class Transform(Component):
    """
    Represents the position, rotation, and scale of a GameObject.

    Attributes:
        position (tuple): The (x, y) coordinates.
        rotation (float): The rotation angle in degrees.
        scale (tuple): The (x, y) scale.
    """

    def __init__(self, position=(0, 0), rotation=0.0, scale=(1.0, 1.0)):
        """
        Initializes a new Transform.

        Args:
            position (tuple, optional): The (x, y) coordinates. Defaults to (0, 0).
            rotation (float, optional): The rotation angle. Defaults to 0.0.
            scale (tuple, optional): The (x, y) scale. Defaults to (1.0, 1.0).
        """
        super().__init__()
        self.position = position
        self.rotation = rotation
        self.scale = scale

class Script(Component):
    """
    Base class for user-defined scripts attached to GameObjects.

    Users should override the Start, Update, and End methods.
    """

    def start(self):
        """
        Called when the GameObject is created.
        """
        pass

    def update(self):
        """
        Called every frame.
        """
        pass

    def end(self):
        """
        Called when the GameObject is destroyed.
        """
        pass

class Input:
    """
    Handles user input.

    Class Methods:
        get_key(key): Returns True if the specified key is pressed.
        get_mouse_position(): Returns the current mouse position.
    """

    @staticmethod
    def get_key(key):
        """
        Checks if a key is currently pressed.

        Args:
            key (str): The key to check (e.g., "W", "SPACE", "LEFT").

        Returns:
            bool: True if the key is pressed, False otherwise.
        """
        # (Replace with your actual input handling logic)
        return False  # Placeholder

    @staticmethod
    def get_mouse_position():
        """
        Returns the current mouse position.

        Returns:
            tuple: The (x, y) coordinates of the mouse.
        """
        # (Replace with your actual input handling logic)
        return (0, 0)  # Placeholder

class Scene:
    """
    Represents a game scene containing GameObjects.

    Attributes:
        game_objects (list): A list of GameObjects in the scene.
    """

    def __init__(self):
        """
        Initializes a new Scene.
        """
        self.game_objects = []

    def add_game_object(self, game_object):
        """
        Adds a GameObject to the scene.

        Args:
            game_object (GameObject): The GameObject to add.
        """
        self.game_objects.append(game_object)

    def remove_game_object(self, game_object):
        """
        Removes a GameObject from the scene.

        Args:
            game_object (GameObject): The GameObject to remove.
        """
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)
            
