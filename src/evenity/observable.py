"""Ovservable class"""
import weakref

class Observable:
    """Observable class"""

    def __init__(self):
        self._observers = weakref.WeakValueDictionary()

    def register_observer(self, observer):
        """Register an observer"""
        self._observers[id(observer)] = observer

    def notify_observers(self, listener, event):
        """Notify all observers"""
        for oid in self._observers:
            self._observers[oid].notify(listener, event)

    def deregister_observer(self, observer):
        """Deregister an observer"""
        self._observers.remove(id(observer))