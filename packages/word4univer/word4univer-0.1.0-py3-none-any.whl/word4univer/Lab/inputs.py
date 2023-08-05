from typing import Type


class Inputs:

    def __init__(self, **inputs: Type):
        """
        Class for storing inputs for lab
        :param inputs: Input keys and their types
        """
        self.keys = list(inputs.keys())
        self.types = list(inputs.values())
        self.values = [None for _ in range(len(self.keys))]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self) -> tuple[str, Type]:
        self.index += 1
        if self.index <= len(self.keys):
            return self.keys[self.index - 1], self.types[self.index - 1]
        else:
            raise StopIteration()

    def get(self, key: str, default=None) -> any:
        try:
            return self.values[self.keys.index(key)]
        except ValueError:
            return default

    def get_type(self, key: str, default=None) -> Type:
        try:
            return self.types[self.keys.index(key)]
        except ValueError:
            return default

    def set(self, key: str, val: any) -> None:
        index = self.keys.index(key)
        if type(val) is self.types[index]:
            self.values[index] = val
        else:
            raise ValueError(f"Param {key} must be {self.types[index]}, got {type(val)}")
