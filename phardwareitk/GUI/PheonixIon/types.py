import os
import platform

from typing import * # type: ignore

class PIenum():
    def __init__(self, value:int=None) -> None:
        if not value:
            self.value = 0
        else:
            self.value = value
        self.entries = []
        self.start_value = 0
        self.enum_dict = {}
        self.enum = []
        self.reverse_enum_dict = {}

    def create_enum(self, entries:list[str], start_value:int=0) -> None:
        self.entries = entries
        self.value = (len(self.entries) - 1) + start_value
        self.start_value = start_value
        self.enum_dict = {name: idx + start_value for idx, name in enumerate(entries)}
        self.reverse_enum_dict = {idx + start_value: name for idx, name in enumerate(entries)}

        self.enum = list(self.enum_dict.values())

    def access(self, name:str) -> int:
        return self.enum_dict.get(name, None)
    
    def reverse_access(self, val:int) -> str:
        return self.reverse_enum_dict.get(val, None)
    
    def __getitem__(self, item:Union[str, int]) -> Any:
        if isinstance(item, str):
            return self.enum_dict.get(item, None)
        elif isinstance(item, int):
            try:
                return self.enum[item]
            except IndexError:
                return None
        return None

    def __repr__(self) -> str:
        return f"PIenum({self.enum_dict})"

class PIint(int):
    def __init__(self, value:int=0) -> None:
        self.value = value
        super().__init__(value)

    def __repr__(self) -> str:
        return f"PIint({self.value})"

class PIuint(int):
    def __init__(self, value:int=0) -> None:
        if value < 0:
            raise ValueError("PIuint cannot be negative")
        self.value = value
        super().__init__(value)

    def __repr__(self) -> str:
        return f"PIuint({self.value})"

class PIstring(str):
    def __init__(self, value:str="") -> None:
        self.value = value
        super().__init__(value)

    def __repr__(self) -> str:
        return f'PIstring("{self.value}")'
    
_pionevent_types_str = [
    # Window lifecycle
    "CREATE",
    "DESTROY",
    "SHOW",
    "HIDE",
    "FOCUS_GAINED",
    "FOCUS_LOST",
    "RESIZE",
    "MOVE",
    "CLOSE",
    "QUIT",
    "MINIMIZE",
    "MAXIMIZE",
    "RESTORE",
    "ENTER",
    "LEAVE",

    # Mouse
    "MOUSEMOVE",
    "MOUSEDOWN",
    "MOUSEUP",
    "MOUSEWHEEL",
    "MOUSEENTER",
    "MOUSELEAVE",
    "MOUSEDRAG",

    # Mouse buttons (with button info passed in event)
    "LEFT_DOWN",
    "LEFT_UP",
    "RIGHT_DOWN",
    "RIGHT_UP",
    "MIDDLE_DOWN",
    "MIDDLE_UP",

    # Keyboard
    "KEYDOWN",
    "KEYUP",
    "KEYPRESS",  # For character-producing keys
    "TEXTINPUT",  # Unicode / text events

    # Modifier keys
    "SHIFT_DOWN",
    "SHIFT_UP",
    "CTRL_DOWN",
    "CTRL_UP",
    "ALT_DOWN",
    "ALT_UP",
    "META_DOWN",
    "META_UP",

    # Scroll / touch / gestures
    "SCROLL",
    "TOUCHSTART",
    "TOUCHMOVE",
    "TOUCHEND",
    "TOUCHCANCEL",
    "PINCH",
    "ZOOM",

    # Drag and drop
    "DRAGENTER",
    "DRAGOVER",
    "DRAGLEAVE",
    "DROP",

    # App/system level
    "TIMER",
    "IDLE",
    "REDRAW",
    "EXPOSE", # X11

    # Custom / user-defined
    "USER_EVENT",
    "CUSTOM_EVENT",

    # Platform-specific extras
    "INPUTLANGCHANGE",
    "DISPLAYCHANGE",
    "POWERBROADCAST",
    "IME_STARTCOMPOSITION",
    "IME_ENDCOMPOSITION",
]

PIonEvent_Types = PIenum()
PIonEvent_Types.create_enum(_pionevent_types_str, 0)

class PIonEvent:
    """Pheonix Ion Event Class"""
    def __init__(self, typ: Union[int, str], **kwargs) -> None:
        self.type: int = 0

        if isinstance(typ, str):
            self.type = PIonEvent_Types.access(typ)
        else:
            self.type = typ

        self.data = kwargs

    def __repr__(self):
        return f"<PIonEvent type={self.type}, data={self.data}>"