FROM python:3.7-slim-stretch

RUN pip install 'dramatiq[rabbitmq]'
RUN pip install requests

ADD actor.py actor.py
ADD task1.py task1.py
ADD task2.py task2.py
ENTRYPOINT ["/usr/local/bin/dramatiq", "actor"]
