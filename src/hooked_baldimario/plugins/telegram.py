"""KafkaObservervable plugin for event system."""
import telepot
from telepot.loop import MessageLoop
from ..observable import Observable

class AsyncTelegramaObservableConsumer(Observable):
    """EventDispatcher class"""

    def __init__(self, token): # pylint: disable=useless-super-delegation
        super().__init__()
        self.bot = telepot.Bot(token)

    def consume(self):
        """Consume the observable"""
        MessageLoop(self.bot, self.telegram_handler).run_as_thread()

    def telegram_handler(self, message):
        """Telegram handler"""
        self.notify_observers('telegram', message)
