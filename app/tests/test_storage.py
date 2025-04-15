import unittest

from database.commands import Command
from database.session import Session
from database.storage import Storage


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.storage = Storage()

    def test_count_values_and_find_vars(self):
        value = 10
        names = ['A', 'B']
        for name in names:
            cmd_data = Command.parse_input(f'SET {name} {value}')
            self.storage.get_command(cmd_data)

        counts_command = f'COUNTS {value}'
        cmd_counts = Command.parse_input(counts_command)

        count = self.storage.count_value(cmd_counts)
        self.assertEqual(count, 2)

        find_command = f'FIND {value}'
        cmd_find = Command.parse_input(find_command)

        find = self.storage.find_vars(cmd_find)

        self.assertEqual(find, names)
