"""Telegram Example"""
import os
import dotenv
from hooked.observer import Observer # pylint: disable=import
from hooked.event.plugins.telegram import AsyncTelegramaObservableConsumer

dotenv.load_dotenv()

class BotListener(Observer):
    """BotListener class"""

    def __init__(self, observable, chat_ids=None):
        self.chat_ids = chat_ids or []
        super().__init__(observable)
        self.listen("telegram", self.on_telegram)
        self._broadcast('Bot started')

    def _get_bot(self):
        """Get bot instance"""
        return self.observable.bot

    def _broadcast(self, message):
        """Send message to all chat_ids"""
        for saved_chat_id in self.chat_ids:
            self._unicast(saved_chat_id, message)

    def _unicast(self, chat_id, message):
        """Send message to a specific chat_id"""
        self._get_bot().sendMessage(
            chat_id,
            message,
            reply_markup=self._get_keyboard(chat_id)
        )

    def on_telegram(self, message):
        """On telegram event"""
        chat_id = None
        user = None
        is_command = False

        if 'chat' in message:
            user = f"{message['chat']['first_name']} " \
                f"{message['chat']['last_name']} " \
                f"({message['chat']['username']}) " \
                f"[{message['chat']['id']}]"
            chat_id = message['chat']['id']


        if 'entities' in message:
            for entity in message['entities']:
                if entity['type'] == 'bot_command':
                    is_command = True

        if 'text' in message:
            text = message['text']

            if is_command:
                if text.startswith('/start'):
                    print(f'User {user} started the bot')
                    self._broadcast(f'User {user} started the bot')

                elif text.startswith('/hello'):
                    print(f'User {user} is saying "{text}"')
                    self._unicast(chat_id, 'Hi!')

def main():
    """Main function"""
    telegram_consumer = AsyncTelegramaObservableConsumer(
        token=os.environ.get('TOKEN')
    )

    BotListener(telegram_consumer, os.environ.get('CHAT_IDS').split(','))

    telegram_consumer.consume()

if __name__ == '__main__':
    main()
