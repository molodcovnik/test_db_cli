from database.commands import Command
from database.services.help import HELP_TEXT
from database.services.replace_storage import use_current_transaction
from database.transactions import TransactionStorage


class Storage(TransactionStorage):
    """Хранилище информации во время сессии"""

    def __init__(self):
        super().__init__()
        self.storage = dict()

    def _get_storage(self):
        return self.storage

    def get_command(self, data: dict):
        try:
            command = data.get('command', None)

            match command:
                case Command.GET:
                    print(self.get_value(data))
                case Command.SET:
                    self.set_value(data)
                case Command.UNSET:
                    self.delete_value(data)
                case Command.COUNTS:
                    print(self.count_value(data))
                case Command.FIND:
                    self.find_vars(data)
                case Command.BEGIN:
                    self.begin(self.storage)
                case Command.ROLLBACK:
                    self.rollback()
                case Command.COMMIT:
                    self.commit()
                case Command.HELP:
                    self.get_help()

        except AttributeError:
            print("Ошибка в команде")

    @use_current_transaction
    def set_value(self, data: dict):
        if data.get('name') is not None:
            self.storage[data.get('name')] = data.get('value')
            return self.storage
        print("Задайте имя переменной")

    @use_current_transaction
    def get_value(self, data: dict):
        return self.storage.get(data.get('name'))

    @use_current_transaction
    def delete_value(self, data: dict):
        self.storage.pop(data.get('name'), None)
        return self.storage

    @use_current_transaction
    def count_value(self, data: dict):
        values_list = list(self.storage.values())
        return values_list.count(data.get('value'))

    @use_current_transaction
    def find_vars(self, data: dict):
        items = self.storage.items()
        variables = []
        for name, value in items:
            if value == data.get('value'):
                print(name)
                variables.append(name)
        return variables

    def get_help(self):
        print(HELP_TEXT)
