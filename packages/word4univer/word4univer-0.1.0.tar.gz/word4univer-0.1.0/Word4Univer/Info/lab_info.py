from .subject_info import SubjectInfo


class LabInfo:
    """ Class for storing lab info """
    def __init__(self,
                 name: str = "Лабораторная работа",
                 index: int = 0,
                 theme: str = None,
                 subject: SubjectInfo = None):
        self.name = name
        self.index = index
        self.theme = theme

        self.subject = subject if subject is not None else SubjectInfo()
