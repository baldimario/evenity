"""KafkaObservervable plugin for event system."""
from kafka import KafkaConsumer
from ..observable import Observable

class KafkaObservableConsumer(Observable):
    """EventDispatcher class"""

    def __init__(self, servers, group, topics): # pylint: disable=useless-super-delegation
        super().__init__()

        self.consumer = KafkaConsumer(
            bootstrap_servers=servers,
            enable_auto_commit=True,
            group_id=group,
            auto_offset_reset='latest'
	    )

        self.consumer.subscribe(topics=topics)

    def consume(self):
        """Consume the observable"""
        for message in self.consumer:
            self.notify_observers(message.topic, message.value)
