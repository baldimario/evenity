# Evenity - Pluggable event hook libary

## Installation
```sh
pip install evenity
```

## Important Notes!
Observables tracks observers with a weakref, if the reference to the observable is lost the observer automatically does not track the object anymore.
So keep track of the observers in a variable to keep them receive observable events.
It could've happened that when you delete an observer, the observable keeping track of the object made the garbage collector not delete it since it still kept its reference. In this case the observer continued to handle the events.
Currently, however, the reference is maintained through a weakref which is why you need to be careful to keep the observer in a variable otherwise if you lose track of it, the observable will lose track of it and it will die.
This is a safety measure to avoid memory leaks.
(Thanks [krow89](https://github.com/krow89))

## Usage
See examples folder at [https://github.com/baldimario/evenity](https://github.com/baldimario/evenity)

```python
"""Example"""
from evenity.observable import Observable
from evenity.observer import Observer

class EventDispatcher(Observable):
    """EventDispatcher class"""

    def __init__(self):
        super().__init__()

    def dispatch(self, topic, event):
        """Consume the observable"""
        self.notify_observers(topic, event)

class EventListener(Observer):
    """EventListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("test", self.on_test)
        self.listen("foo", self.on_test)

    def on_test(self, event):
        """On test event"""
        print(f"1 {event}")

    def on_foo(self, event):
        """On test event"""
        print(f"2 {event}")

def main():
    dispatcher = EventDispatcher()

    listener = EventListener(dispatcher)

    # Simulate dispatching of some events
    events = [
        ["test", "Hello World!"],
        ["foo", "Foo Bar!"],
    ]

    for event in events:
        dispatcher.dispatch(event[0], event[1])

if __name__ == '__main__':
    main()

# 1 Hello World!
# 2 Foo Bar!
```

### simple.py
This file contains an implementation of observers and observable
It shows how simple is to implement your own observable and register all the observers as you want

## kafka.py
This script contains an implementations of some listeners (observers) for the kafka plugin

This subscribe some listeners for the KafkaObservableConsumer listening for events from many topics

dependency: kafka-python

```python
from evenity.observer import Observer
from evenity.plugins.kafka import KafkaObservableConsumer

class Listener(Observer):
    """ImporterListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("topic1", self.on_topic1)
        self.listen("topic2", self.on_topic2)

    def on_topic1(self, event):
        """On test event"""
        print(event.decode('utf-8'))

    def on_topic2(self, event):
        """On test event"""
        print(event.decode('utf-8'))

consumer = KafkaObservableConsumer(
    servers=os.environ.get('KAFKA_SERVERS').split(','),
    group="mygroup",
    topics=[
        "topic1",
        "topic2"
    ]
)

listener = Listener(consumer)

consumer.consume()
```

## ftp.py 
ftp.py contains an example listener for the ftp observable

This can be useful wen you want to handle file uploaded in an event way

dependency: pyftpdlib

```python
from evenity.observer import Observer
from evenity.event.plugins.ftp import FTPObservableConsumer

class Listener(Observer):
    """FTPListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("ftp", self.on_ftp)

    def on_ftp(self, file):
        """On ftp event"""
        print(f'Got file, path: {file}')
        os.unlink(file)

consumer = FTPObservableConsumer(
    user=os.environ.get('FTP_USER'),
    password=os.environ.get('FTP_PASSWORD'),
    port=os.environ.get('FTP_PORT'),
    path=os.path.join(ABSPATH, os.environ.get('FTP_PATH')),
    host=os.environ.get('FTP_BIND_ADDRESS'),
    on_file_received_event='ftp'
)

listener = Listener(consumer)

consumer.consume()
```

## shell.py
This file contains an example listener for the shell observable

The use case is to read an output steam from a program (or fifo file) and receive an event for each line printed

```python
from evenity.plugins.shell import ShellObservableConsumer
from evenity.observer import Observer

class Listener(Observer):
    """ShellListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.first_run = True
        # self.observable.command
        self.listen('monitor-sensor --accel', self.fetch)

    def fetch(self, line):
        """Update method"""
        print(line)

observable = ShellObservableConsumer('monitor-sensor --accel')
listener = Listener(observable)
observable.consume()
```

## telegram.py
This script contains an example listener for telegram bot events (updates, texts and commands)

The observers will be notified for each telegram bot event

dependency: telepot

```python
import time
from evenity.observer import Observer
from evenity.plugins.telegram import AsyncTelegramaObservableConsumer

class Listener(Observer):
    def __init__(self, observable):
        super().__init__(observable)
        self.listen("telegram", self.on_telegram)

    def on_telegram(self, message):
        if 'chat' in message:
            user = message['username']
            chat_id = message['chat']['id']
            text = message['text']
            self.observable.bot.sendMessage(
                chat_id,
                f'User {user} with chat id {chat_id} sent "{text}"'
            )

consumer = AsyncTelegramaObservableConsumer(
    token=os.environ.get('TOKEN'),
    on_message_received_event='telegram'
)

listener = Listener(consumer)

consumer.consume()

while True:
    time.sleep(10)
```

## ws.py
This scripts contains an example for websocket connection (open, close, error, message)

Handle websocket events

dependency: websocket-client

```python
from evenity.plugins.websocket import WebsocketObservable
from evenity.observer import Observer

class Listener(Observer):
    """Websocket listener."""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("message", self.on_message)
        self.listen("close", self.on_close)
        self.listen("error", self.on_error)
        self.listen("open", self.on_open)

    def on_message(self, event):
        """Update websocket listener."""
        websocket = event['websocket']
        message = event['event']
        print(websocket, message)

    def on_error(self, event):
        """Update websocket listener."""
        websocket = event['websocket']
        message = event['event']
        print(websocket, message)

    def on_open(self, event):
        """Update websocket listener."""
        websocket = event['websocket']
        message = event['event']
        print(websocket, message)

    def on_close(self, event):
        """Update websocket listener."""
        websocket = event['websocket']
        message = event['event']
        print(websocket, message)

consumer = WebsocketObservable(
    "wss://localhost/foo",
    on_open_event='open',
    on_error_event='error',
    on_close_event='close',
    on_message_event='message'
)

listener = Listener(consumer)

consumer.consume()
```

## SimpleObserver

You can use the SimpleObserver to create observers without defining a new class but using callbacks instead

```python
from evenity.observer import SimpleObserver
from evenity.plugins.kafka import KafkaObservableConsumer

consumer = KafkaObservableConsumer(
    servers=os.environ.get('KAFKA_SERVERS').split(','),
    group="mygroup",
    topics=[
        "topic1",
        "topic2"
    ]
)

def on_topic1(event):
    """On test event"""
    print(event.decode('utf-8'))

listener = SimpleObserver(consumer, {
    'topic1': on_topic1,
    'topic2': lambda event: print(event.decode('utf-8'))
})

consumer.consume()
```
