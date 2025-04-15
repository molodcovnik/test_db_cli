"""
Команды:
SET - сохраняет аргумент в базе данных.
GET - возвращает, ранее сохраненную переменную. Если такой переменной
не было сохранено, возвращает NULL
UNSET - удаляет, ранее установленную переменную. Если значение не было
установлено, не делает ничего.
COUNTS - показывает сколько раз данные значение встречается в базе данных.
FIND - выводит найденные установленные переменные для данного значения.
END - закрывает приложение.
"""
import re


class TransactionCommand:
    """Команды для транзакций"""

    BEGIN = "BEGIN" ### начало транзакции.
    ROLLBACK = "ROLLBACK" ### откат текущей (самой внутренней) транзакции
    COMMIT = "COMMIT" ### фиксация изменений текущей (самой внутренней) транзакции


class Command(TransactionCommand):
    """Общие команды для терминала"""

    GET = "GET" ### return var or None
    SET = "SET"
    COUNTS = "COUNTS" ### показывает сколько раз данные значение встречается в базе данных.
    UNSET = "UNSET" ### удаление
    FIND = "FIND" ### выводит найденные установленные переменные для данного значения.
    END = "END" ### закрывает приложение.
    HELP = "HELP" ### Справка

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
