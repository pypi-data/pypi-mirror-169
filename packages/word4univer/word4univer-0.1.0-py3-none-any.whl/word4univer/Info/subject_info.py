from ..Name import FullName


class SubjectInfo:
    """ Class for storing subject info (name, teacher's full name) """
    def __init__(self,
                 name: str = "Название предмета",
                 teacher: FullName = None):
        self.name = name
        self.teacher = teacher if teacher is not None else FullName()

    def __str__(self):
        return self.name
