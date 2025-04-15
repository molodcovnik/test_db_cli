import string
import unittest

from database.commands import Command
from database.session import Session
from database.storage import Storage


class TestRunApplication(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.storage = Storage()
        self.vars_name = list(string.ascii_lowercase)
        self.values = [i for i in range(1, 27)]

    def test_ok(self):
        value = 10
        name = 'A'
        cmd_data_set = Command.parse_input(f'SET {name} {value}')
        self.storage.get_command(cmd_data_set)

        result = self.storage._get_storage()
        self.assertEqual(result.get(name), value)

    def test_mass_set_and_get_vars(self):
        for name, value in zip(self.vars_name, self.values):
            cmd_data = Command.parse_input(f'SET {name} {value}')
            self.storage.get_command(cmd_data)

        result = self.storage._get_storage()

        self.assertEqual(result.get('A'), 1)
        self.assertEqual(result.get('B'), 2)
        self.assertEqual(result.get('C'), 3)
        self.assertEqual(result.get('Z'), 26)

        cmd_delete = Command.parse_input('UNSET D')
        self.storage.get_command(cmd_delete)

        result_after_delete = self.storage._get_storage()
        self.assertEqual(result_after_delete.get('D'), None)

    def test_transaction(self):
        """Тестируем транзакцию, устанавливаем значение, потом изменяем его, откатываем и сохраняем"""

        cmd_data_a = Command.parse_input(f'SET A 10')
        self.storage.get_command(cmd_data_a)

        cmd_data_b = Command.parse_input(f'SET B 20')
        self.storage.get_command(cmd_data_b)

        storage = self.storage._get_storage()
        self.assertEqual(storage.get('A'), 10)
        self.assertEqual(storage.get('B'), 20)

        cmd_begin = Command.parse_input('BEGIN')
        self.storage.get_command(cmd_begin)

        cmd_data_a_begin = Command.parse_input(f'SET A 30')
        self.storage.get_command(cmd_data_a_begin)

        transaction_stack_first = self.storage._get_transaction_stack()
        self.assertEqual(transaction_stack_first[-1].get('A'), 30)

        cmd_begin_two = Command.parse_input('BEGIN')
        self.storage.get_command(cmd_begin_two)

        cmd_data_a_begin_two = Command.parse_input(f'SET A 50')
        self.storage.get_command(cmd_data_a_begin_two)

        transaction_stack_two = self.storage._get_transaction_stack()
        self.assertEqual(transaction_stack_two[-1].get('A'), 50)

        cmd_rollback = Command.parse_input('ROLLBACK')
        self.storage.get_command(cmd_rollback)

        cmd_commit = Command.parse_input('COMMIT')
        self.storage.get_command(cmd_commit)

        last_data_in_storage = self.storage._get_storage()

        self.assertEqual(last_data_in_storage.get('A'), 30)
        self.assertEqual(last_data_in_storage.get('B'), 20)
