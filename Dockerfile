FROM python:3.9.1

RUN mkdir /django
WORKDIR /django

COPY requirements.txt /django/

RUN pip install --no-compile --no-cache-dir --upgrade pip && \ 
    pip install --no-compile --no-cache-dir -r requirements.txt

