FROM python:3.12

COPY configs .
COPY migrations .
COPY src .

RUN pip install -r requirements.txt

EXPOSE 8000
