"""Shell plugin for event system."""
import subprocess
from ..observable import Observable

class ShellObservableConsumer(Observable):
    """EventDispatcher class"""

    def __init__(self, command): # pylint: disable=useless-super-delegation
        super().__init__()
        self.command = command
        cmd = ['/usr/bin/bash', '-c', self.command]
        self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    def consume(self):
        """Consume the observable"""
        while True:
            line = self.process.stdout.readline().strip().decode('utf-8')
            self.notify_observers(self.command, line)
