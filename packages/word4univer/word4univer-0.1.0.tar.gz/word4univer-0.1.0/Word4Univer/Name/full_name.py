from .name_pattern import NamePattern


class FullName:
    """ Class for storing names """
    def __init__(self,
                 surname: str = "Иванов",
                 name: str = "Иван",
                 patronymic: str = "Иванович"):
        self.surname = surname.title()
        self.name = name.title()
        self.patronymic = patronymic.title()

    def format(self, pattern: NamePattern | str) -> str:
        if pattern is not NamePattern:
            pattern = NamePattern(pattern)
        return pattern.get_str(self.surname, self.name, self.patronymic)

    def __str__(self):
        return ' '.join([self.surname, self.name, self.patronymic])
