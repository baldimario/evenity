from evenity.observable import Observable
import websocket

class WebsocketObservable(Observable):
    """Websocket observable."""

    def __init__(self,
            connection_url,
            on_open_event='open',
            on_message_event='message',
            on_error_event='event',
            on_close_event='close'
        ):
        """Initialize websocket observable."""
        super().__init__()
        self.connection_url = connection_url
        self.on_open_event = on_open_event
        self.on_message_event = on_message_event
        self.on_error_event = on_error_event
        self.on_close_event = on_close_event

    def consume(self):
        """Consume the observable"""
        self.websocket = websocket.WebSocketApp(self.connection_url,
            on_open = self.on_open,
            on_message = self.on_message,
            on_error = self.on_error,
            on_close = self.on_close
        )

        self.websocket.run_forever()

    def on_error(self, ws, error):
        """On error handler"""
        self.notify_observers(self.on_error_event, {
            'websocket': self.websocket,
            'event': error,
        })

    def on_close(self, ws):
        """On close handler"""
        self.notify_observers('close', {
            'websocket': self.websocket,
            'event': 'closed',
        })
    
    def on_message(self, ws, message):
        """On message handler"""
        self.notify_observers('message', {
            'websocket': self.websocket,
            'event': message,
        })
    
    def on_open(self, ws):
        """On open handler"""
        self.notify_observers('open', {
            'websocket': self.websocket,
            'event': 'opened',
        })