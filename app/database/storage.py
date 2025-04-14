from database.commands import Command


class Storage:
    """Хранилище информации во время сессии"""

    def __init__(self):
        self.storage = dict()

    def get_command(self, data: dict):
        command = data.get('command')
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

    def get_storage(self):
        return self.storage

    def set_value(self, data: dict):
        if data.get('name') is not None:
            self.storage[data.get('name')] = data.get('value')
            return self.storage
        print("Задайте имя переменной")

    def get_value(self, data: dict):
        return self.storage.get(data.get('name'))

    def delete_value(self, data: dict):
        self.storage.pop(data.get('name'), None)
        return self.storage

    def count_value(self, data: dict):
        values_list = list(self.storage.values())
        return values_list.count(data.get('value'))

    def find_vars(self, data: dict):
        items = self.storage.items()
        for name, value in items:  # for name, age in dictionary.iteritems():  (for Python 2.x)
            if value == data.get('value'):
                print(name)
