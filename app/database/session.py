from database.commands import Command
from database.services.help import START_TEXT


class Session:
    @staticmethod
    def get_session():
        print(START_TEXT)
        try:
            while True:
                command = input("Введите команду: ")
                if command.upper() == Command.END:
                    break
                yield command
        except EOFError:
            print('\nСессия закрыта!')
        except KeyboardInterrupt:
            print("\nПользователь закрыл сессию.")
