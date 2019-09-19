import dramatiq
import requests


def wc(url):
    response = requests.get(url)
    count = len(response.text.split(" "))
    print(f"There are {count} words at {url!r}.")


@dramatiq.actor
def count_words(url):
    wc(url)
