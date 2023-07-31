import unittest
from evenity.observable import Observable
from evenity.observer import Observer, SimpleObserver

class EventDispatcher(Observable):
    """EventDispatcher class"""

    def __init__(self): # pylint: disable=useless-super-delegation
        super().__init__()

    def dispatch(self, topic, event):
        """Consume the observable"""
        self.notify_observers(topic, event)

class TestSimple(unittest.TestCase):

    def test_upper(self):
        expected_events = [
            "1 Hello World!",
            "2 Foo Bar!",
        ]
        received_events = []

        dispatcher = EventDispatcher()
        SimpleObserver(dispatcher, {
            'test': lambda event: received_events.append("1 " + event),
            'foo': lambda event: received_events.append("2 " + event)
        })

        events = [
            ["test", "Hello World!"],
            ["foo", "Foo Bar!"],
        ]

        for event in events:
            dispatcher.dispatch(event[0], event[1])

        self.assertEqual(expected_events, received_events)

if __name__ == '__main__':
    unittest.main()

