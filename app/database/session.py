from database.commands import Command
from database.storage import Storage


class Session:
    @staticmethod
    def get_session():
        while True:
            command = input("Введите команду (GET A, SET A 10): ")
            if command.upper() == Command.END:
                break
            yield command
