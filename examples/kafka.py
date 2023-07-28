"""Kafka example"""
import os
import json
from dotenv import load_dotenv
from hooked.observer import Observer # pylint: disable=import-error
from hooked.plugins.kafka import KafkaObservableConsumer # pylint: disable=import-error

class ImporterListener(Observer):
    """ImporterListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("toImport", self.on_import)

    def on_import(self, event):
        """On test event"""
        data = json.loads(event.decode('utf-8'))
        print(f"Importer: {data['platform_website']} {data['canonical_url']}")

class ReleaserListener(Observer):
    """ReleaserListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("released", self.on_import)

    def on_import(self, event):
        """On test event"""
        data = json.loads(event.decode('utf-8'))
        print(f"Releaser: {data['id']}")

def main():
    """Main function"""

    load_dotenv()

    consumer = KafkaObservableConsumer(
        servers=os.environ.get('KAFKA_SERVERS').split(','),
        group="healthcheck",
        topics=[
            "toImport",
            "released"
        ]
    )

    ImporterListener(consumer)
    ReleaserListener(consumer)

    consumer.consume()

if __name__ == '__main__':
    main()
