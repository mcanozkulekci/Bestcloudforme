FROM ubuntu:20.04


RUN apt-get update -y && \
    apt-get install -y python3-pip


COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
EXPOSE 5001


ENTRYPOINT [ "python3" ,"api.py"]

