FROM python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /home/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
