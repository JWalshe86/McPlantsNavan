FROM python:3.11-slim-bookworm
ENV PYTHONUNBUFFERED=1
WORKDIR /navanplants
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt





