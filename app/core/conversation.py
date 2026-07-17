import time


class ConversationManager:

    def __init__(self):
        self.awake = False
        self.last_command_time = time.time()

    def wake(self):
        self.awake = True
        self.last_command_time = time.time()

    def sleep(self):
        self.awake = False

    def is_awake(self):
        return self.awake

    def update(self):
        self.last_command_time = time.time()

    def timeout(self, seconds=30):
        if not self.awake:
            return False

        return (time.time() - self.last_command_time) > seconds


conversation = ConversationManager()