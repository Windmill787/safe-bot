FROM python:3.10.4-slim-buster

RUN python3 -m pip install telethon
RUN python3 -m pip install python-telegram-bot

WORKDIR /app

COPY main.py ./
COPY session_name.session ./

CMD [ "python3", "./main.py", "", ""]