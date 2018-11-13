import dramatiq
import requests
from dramatiq.brokers.rabbitmq import RabbitmqBroker


def wc(url):
    response = requests.get(url)
    count = len(response.text.split(" "))
    print(f"There are {count} words at {url!r}.")


broker1 = RabbitmqBroker(
    host="rabbit",
    port=5672,
    heartbeat=5,
    connection_attempts=5,
    blocked_connection_timeout=30,
)
# For it to work, just uncomment next line
# dramatiq.broker.set_broker(broker1)


class WordCounter(dramatiq.GenericActor):
    class Meta:
        broker = broker1

    def perform(self, url):
        wc(url)


@dramatiq.actor(broker=broker1)
def count_words(url):
    wc(url)


WordCounter.send("http://example.com")
count_words.send("http://example.com")
