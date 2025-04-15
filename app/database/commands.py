"""

"""
import re


class TransactionCommand:
    """Команды для транзакций"""

    BEGIN = "BEGIN"
    ROLLBACK = "ROLLBACK"
    COMMIT = "COMMIT"


class Command(TransactionCommand):
    """Общие команды для терминала"""

    GET = "GET"
    SET = "SET"
    COUNTS = "COUNTS"
    UNSET = "UNSET"
    FIND = "FIND"
    END = "END"
    HELP = "HELP"

    @classmethod
    def get_all_commands(cls):
        return [cls.GET, cls.SET, cls.COUNTS, cls.UNSET, cls.FIND, cls.END, cls.BEGIN, cls.ROLLBACK, cls.COMMIT, cls.HELP]

    @classmethod
    def get_command(cls, value: str):
        all_commands = cls.get_all_commands()
        if value.upper() in all_commands:
            return value.upper()
        return None

    @classmethod
    def get_variable_name(cls, string: str):
        line = string.split()[1:]
        new_string = " ".join(word for word in line)
        match = re.search(r'\b[A-Za-z_][A-Za-z0-9_]*\b', new_string)
        if match:
            word = match.group()
            return word.upper()
        return None

    @classmethod
    def get_value(cls, string: str):
        match = re.search(r'\b\d+\b', string)
        if match:
            return int(match.group())
        return None

    @classmethod
    def parse_input(cls, string: str):
        """Парсим входную строку на команду, переменную и значение"""

        all_commands = cls.get_all_commands()

        len_arguments = len(string.split())

        match len_arguments:
            case 0:
                return "Аргументы не получены"
            case 1:
                cmd = string.split()[0]
                if cmd.upper() not in all_commands:
                    return "Команда не найдена"

                data = {
                    'command': cls.get_command(cmd),
                    'name': cls.get_variable_name(string),
                    'value': cls.get_value(string)
                }

                return data
            case 2:
                cmd = string.split()[0]
                if cmd.upper() not in all_commands:
                    return "Команда не найдена"

                data = {
                    'command': cls.get_command(cmd),
                    'name': cls.get_variable_name(string),
                    'value': cls.get_value(string)
                }
                return data
            case 3:
                cmd = string.split()[0]
                if cmd.upper() not in all_commands:
                    return "Команда не найдена"

                data = {
                    'command': cls.get_command(cmd),
                    'name': cls.get_variable_name(string),
                    'value': cls.get_value(string)
                }

                return data
            case 4:
                arg = string.split()[-1]
                return f"Лишний аргумент {arg}"
