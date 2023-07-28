"""Simple Example"""
from hooked.observable import Observable
from hooked.observer import Observer

class EventDispatcher(Observable):
    """EventDispatcher class"""

    def __init__(self): # pylint: disable=useless-super-delegation
        super().__init__()

    def dispatch(self, topic, event):
        """Consume the observable"""
        self.notify_observers(topic, event)

class EventListener1(Observer):
    """EventListener1 class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("test", self.on_test)

    def on_test(self, event):
        """On test event"""
        print(f"1 {event}")

class EventListener2(Observer):
    """EventListener2 class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("test", self.on_test)
        self.listen("foo", self.on_foo)

    def on_test(self, event):
        """On test event"""
        print(f"2: {event}")

    def on_foo(self, event):
        """On test event"""
        print(f"2 {event}")

def main():
    """Main function"""
    # Create the dispatcher that consume messages and notify observers
    dispatcher = EventDispatcher()

    EventListener1(dispatcher)
    EventListener2(dispatcher)

    # Simulate dispatching of some events
    events = [
        ["test", "Hello World!"],
        ["foo", "Foo Bar!"],
    ]

    for event in events:
        dispatcher.dispatch(event[0], event[1])

if __name__ == '__main__':
    main()
