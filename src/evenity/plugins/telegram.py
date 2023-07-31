"""KafkaObservervable plugin for event system."""
import telepot
from telepot.loop import MessageLoop
from ..observable import Observable

class AsyncTelegramaObservableConsumer(Observable):
    """EventDispatcher class"""

    def __init__(self, token, on_message_received_event='telegram'): # pylint: disable=useless-super-delegation
        super().__init__()
        self.on_message_received_event = on_message_received_event
        self.bot = telepot.Bot(token)

    def consume(self):
        """Consume the observable"""
        MessageLoop(self.bot, self.telegram_handler).run_as_thread()

    def telegram_handler(self, message):
        """Telegram handler"""
        self.notify_observers(self.on_message_received_event, message)
