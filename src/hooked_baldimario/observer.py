"""Observer class"""

class Observer:
    """Observer class"""

    def __init__(self, observable):
        self._listeners = {}
        observable.register_observer(self)

    def notify(self, listener, event):
        """Notify the observer"""
        if listener in self._listeners:
            self._listeners[listener](event)

    def listen(self, event, callback):
        """Listen to an event"""
        self._listeners[event] = callback
