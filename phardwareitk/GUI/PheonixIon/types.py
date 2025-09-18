import os
import platform

from typing import * # type: ignore

class PIenum(list):
    def __init__(self, value:int=None) -> None:
        if not value:
            self.value = 0
        else:
            self.value = value
        self.entries = []
        self.start_value = 0
        self.enum_dict = {}

    def create_enum(self, entries:list[str], start_value:int=0) -> None:
        self.entries = entries
        self.value = (len(self.entries) - 1) + start_value
        self.start_value = start_value
        self.enum_dict = {name: idx + start_value for idx, name in enumerate(entries)}

        super().__init__(self.enum_dict.values())

    def access(self, name:str) -> int:
        return self.enum_dict.get(name, None)

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