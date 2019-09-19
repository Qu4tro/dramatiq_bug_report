import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker


broker1 = RabbitmqBroker(
    host="rabbit",
    port=5672,
    heartbeat=5,
    connection_attempts=5,
    blocked_connection_timeout=30,
)

broker2 = RabbitmqBroker(
    host="rabbit",
    port=5672,
    heartbeat=5,
    connection_attempts=5,
    blocked_connection_timeout=30,
)

dramatiq.set_broker(broker1)
from task1 import WordCounter

WordCounter.send("http://example.com")

from task2 import count_words

dramatiq.set_broker(broker2)
count_words.send("http://example.com")
