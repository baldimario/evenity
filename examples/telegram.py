"""Telegram Example"""
import os
import dotenv
from evenity.observer import Observer # pylint: disable=import
from evenity.plugins.telegram import AsyncTelegramaObservableConsumer

dotenv.load_dotenv()

class BotListener(Observer):
    """BotListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("telegram", self.on_telegram)

    def _get_bot(self):
        """Get bot instance"""
        return self.observable.bot

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
                    self._get_bot().sendMessage(
                        chat_id,
                        f'User {user} started the bot'
                    )

                elif text.startswith('/hello'):
                    print(f'User {user} is saying "{text}"')
                    self._get_bot().sendMessage(
                        chat_id,
                        'Hi!'
                    )

def main():
    """Main function"""
    telegram_consumer = AsyncTelegramaObservableConsumer(
        token=os.environ.get('TOKEN'),
        on_message_received_event='telegram'
    )

    BotListener(telegram_consumer)

    telegram_consumer.consume()

if __name__ == '__main__':
    main()
