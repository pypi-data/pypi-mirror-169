from ..Name import FullName


class StudentInfo:
    """ Class for representing student (full name and variant) """

    def __init__(self,
                 name: FullName = None,
                 group: str = "Group",
                 var: int = 0):
        self.name = name if name is not None else FullName()
        self.group = group
        self.variant = var

    def __str__(self):
        return self.name
