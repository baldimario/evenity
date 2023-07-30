"""Websocket Observable Class"""
import sys
sys.path.append(".")
from evenity.plugins.websocket import WebsocketObservable
from evenity.observer import Observer

class WebSocketListener(Observer):
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


def main():
    """Main function."""
    consumer = WebsocketObservable(
        "wss://demo.piesocket.com/v3/channel_123?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self",
        on_open_event='open', # optional, default 'open'
        on_error_event='error', # optional, default 'error'
        on_close_event='close', # optional, default 'close'
        on_message_event='message' # optional, default 'message'
    )
    WebSocketListener(consumer)
    consumer.consume()

if __name__ == '__main__':
    main()