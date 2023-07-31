"""KafkaObservervable plugin for event system."""
from pyftpdlib.authorizers import DummyAuthorizer # pylint: disable=import-error
from pyftpdlib.handlers import FTPHandler # pylint: disable=import-error
from pyftpdlib.servers import FTPServer # pylint: disable=import-error
from ..observable import Observable

class FTPObservableConsumer(Observable):
    """EventDispatcher class"""
    class CustomHandler(FTPHandler):
        """CustomHandler class"""
        def on_file_received(self, file):
            """On file received"""
            self.observable.on_file_received(file)

    def __init__(self, host='0.0.0.0', user='admin', password='12345', port=21, path='./storage', on_file_received_event='ftp'): # pylint: disable=useless-super-delegation
        super().__init__()
        self.on_file_received_event = on_file_received_event
        authorizer = DummyAuthorizer()
        authorizer.add_user(user, password, path, perm="elradfmwMT")
        handler = self.CustomHandler
        handler.observable = self
        handler.authorizer = authorizer
        handler.passive_ports = range(60000, 65535)
        handler.permit_foreign_addresses = True
        self.server = FTPServer((host, port), handler)

    def consume(self):
        """Consume the observable"""
        self.server.serve_forever()

    def on_file_received(self, file):
        """On file received"""
        self.notify_observers(self.on_file_received_event, file)
