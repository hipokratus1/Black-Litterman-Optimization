FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

COPY . ./app

RUN pip install --user -r ./app/requirements.txt

WORKDIR /app


