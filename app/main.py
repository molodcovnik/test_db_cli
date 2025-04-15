from database.session import Session
from database.commands import Command
from database.storage import Storage


def main():
    session = Session()
    storage = Storage()
    session_generator = session.get_session()
    for command in session_generator:
        cmd_data = Command.parse_input(command)
        storage.get_command(cmd_data)


if __name__ == "__main__":
    main()
