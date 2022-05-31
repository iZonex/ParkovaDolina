FROM python:3.11.0b1-buster

RUN mkdir /bot
COPY app.py /bot/app.py
COPY requirements.txt /bot/requirements.txt
WORKDIR /bot/
RUN pip install -r requirements.txt
CMD python app.py