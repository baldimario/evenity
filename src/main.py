
from evenity.observable import Observable
from evenity.observer import Observer, SimpleObserver

class EventDispatcher(Observable):
    """EventDispatcher class"""

    def __init__(self): # pylint: disable=useless-super-delegation
        super().__init__()

    def dispatch(self, topic, event):
        """Consume the observable"""
        self.notify_observers(topic, event)

def main():
    expected_events = [
        "1 Hello World!",
        "2 Foo Bar!",
    ]
    received_events = []

    dispatcher = EventDispatcher()
    observer = SimpleObserver(dispatcher, {
        'test': lambda event: received_events.append("1 " + event),
        'foo': lambda event: received_events.append("2 " + event)
    })

    events = [
        ["test", "Hello World!"],
        ["foo", "Foo Bar!"],
    ]

    observer = None

    for event in events:
        dispatcher.dispatch(event[0], event[1])

    print(received_events)

if __name__ == '__main__':
    main()