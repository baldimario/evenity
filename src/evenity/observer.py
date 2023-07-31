"""Observer class"""

class Observer:
    """Observer class"""

    def __init__(self, observable):
        self._listeners = {}
        self.observable = observable
        self.register(observable)

    def register(self, observable):
        """Register to an observable"""
        observable.register_observer(self)

    def notify(self, listener, event):
        """Notify the observer"""
        if listener in self._listeners:
            self._listeners[listener](event)

    def listen(self, event, callback):
        """Listen to an event"""
        self._listeners[event] = callback

class SimpleObserver(Observer):
    """SimpleObserver class"""

    def __init__(self, observable, callback_lookup):
        super().__init__(observable)
        for event, callback in callback_lookup.items():
            self.listen(event, callback)