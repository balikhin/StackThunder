from random import randint
from time import sleep

from robot.robot import Robot


def db_engine_run_command(db_url: str, command: str):
    """
    Shit to use for db access
    """
    print('I run this command %r in db %r' % (command, db_url))
    return ['CrapStack,n/a,123.dll']


class Server:
    """
    Server
    """
    def __init__(self, db_url, chunk_size):
        self.db_url = db_url
        self.chunk_size = chunk_size
        Robot.WHITE_LIST = self._get_white_list()

    def _get_white_list(self) -> list:
        return []

    def run(self):
        """
        Server start
        """
        while True:
            stacks = self.get_stacks()
            if not stacks:
                sleep(60)
                continue

            for stack in stacks:
                result = Robot.run(stack)
                self.send_result({'stack': stack, 'result': result})

    def get_stacks(self):
        # TODO: FIX ME WITH MT API KNOWLEDGE
        return db_engine_run_command(self.db_url, 'Please get me some sweed stack')

    def send_result(self, result: dict):
        print('I send data back to %r is: %r' % (self.db_url, result))


server = Server('mysql://noooooda.com/stack_db', chunk_size=400)
server.run()
