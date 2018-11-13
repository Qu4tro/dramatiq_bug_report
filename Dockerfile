FROM python:3.7-slim-stretch

RUN pip install 'dramatiq[rabbitmq]'
RUN pip install requests

ADD actor.py actor.py
ENTRYPOINT ["/usr/local/bin/dramatiq", "actor"]
