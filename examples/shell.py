"""Shell Example"""
from evenity.plugins.shell import ShellObservableConsumer
from evenity.observer import Observer

class ShellListener(Observer):
    """ShellListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.first_run = True
        self.listen(self.observable.command, self.fetch)

    def fetch(self, line):
        """Update method"""
        print(line)

def main():
    """Main function"""
    observable = ShellObservableConsumer('monitor-sensor --accel')
    listener = ShellListener(observable)
    observable.consume()

if __name__ == '__main__':
    main()
