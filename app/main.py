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

from database.session import Session
from database.commands import Command
from database.storage import Storage

"""
Пример
> GET A
NULL
> SET A 10
> GET A
10
> COUNTS 10
1
> SET B 20
> SET C 10
> COUNTS 10
2
> UNSET B
> GET B
NULL
> END
"""


def main():
    session = Session()
    storage = Storage()
    session_generator = session.get_session()
    for command in session_generator:
        cmd_data = Command.parse_input(command)
        storage.get_command(cmd_data)
        # storage.get_storage()
        # c = Command(cmd)
        # c.print_data()
        # session.storage.set_value(cmd)


if __name__ == "__main__":
    main()
