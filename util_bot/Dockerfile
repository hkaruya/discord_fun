# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /util_bot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY bot.py bot.py

CMD ["python3", "bot.py"]
