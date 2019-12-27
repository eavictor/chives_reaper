FROM python:3.7.6-buster

COPY ./src /src
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "-m", "/src/bot.py"]