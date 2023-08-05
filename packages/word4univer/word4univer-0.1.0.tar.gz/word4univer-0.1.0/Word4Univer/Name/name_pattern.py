class NamePattern:
    """ Pattern for parsing and formatting full name """

    def __init__(self, pattern: str = None):
        if pattern is None:
            pattern = 'SNP'

        self.__positions = []
        self.update_pattern(pattern)

    def update_pattern(self, pattern: str) -> None:
        """
        Method for applying new pattern
        @param pattern: pattern string (S,s - surname, N,n - name, P,p - patronymic, and lowercase for initials)
        """

        self.__positions = [x for x in pattern if x.upper() in ['S', 'N', 'P']]

    def get_list(self, surname: str = '', name: str = '', patronymic: str = '') -> list[str]:
        """
        Method for ordering full name
        @return: List with ordered full name
        """
        items = {'S': surname, 'N': name, 'P': patronymic}

        fullname = []
        for pos in self.__positions:
            word = items[pos.upper()]
            if pos.islower():
                word = word[0] + '.'
            fullname.append(word)

        return fullname

    def get_str(self, surname: str = '', name: str = '', patronymic: str = '') -> str:
        """
        Method for ordering full name
        @return: String with ordered full name
        """
        return ' '.join(self.get_list(surname, name, patronymic))

    def parse_list(self, *full_name: str) -> tuple[str, str, str]:
        """
        Method for parsing list with surname name and patronymic according to pattern
        @param full_name: surname name and patronymic ordered by pattern
        @return: tuple (surname, name, patronymic)
        """
        parts = {}
        for pos, item in enumerate(full_name):
            if pos >= len(self.__positions):
                break
            parts[self.__positions[pos].upper()] = item if item else ""

        return str(parts.get('S', '')), str(parts.get('N', '')), str(parts.get('P', ''))

    def parse_str(self, full_name: str) -> tuple[str, str, str]:
        """
        Method for parsing string with surname name and patronymic according to pattern
        @param full_name: sting with full_name, ordered by pattern
        @return: tuple (surname, name, patronymic)
        """
        return self.parse_list(*full_name.split())

    def __str__(self):
        return ''.join(self.__positions)
