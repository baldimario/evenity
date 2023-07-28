"""Ovservable class"""

class Observable:
    """Observable class"""

    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        """Register an observer"""
        self._observers.append(observer)

    def notify_observers(self, listener, event):
        """Notify all observers"""
        for obs in self._observers:
            obs.notify(listener, event)
