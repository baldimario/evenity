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

    def __init__(self, user='admin', password='12345', port=21, path='./storage'): # pylint: disable=useless-super-delegation
        super().__init__()
        authorizer = DummyAuthorizer()
        authorizer.add_user(user, password, path, perm="elradfmwMT")
        handler = self.CustomHandler
        handler.observable = self
        handler.authorizer = authorizer
        handler.passive_ports = range(60000, 65535)
        handler.permit_foreign_addresses = True
        self.server = FTPServer(("0.0.0.0", port), handler)

    def consume(self):
        """Consume the observable"""
        self.server.serve_forever()

    def on_file_received(self, file):
        """On file received"""
        self.notify_observers('ftp', file)
