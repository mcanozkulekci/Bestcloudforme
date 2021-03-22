FROM ubuntu:20.04


RUN apt-get update -y && \
    apt-get install -y python3-pip


COPY . /api
WORKDIR /api

RUN pip3 install -r requirements.txt



ENTRYPOINT [ "python3"]
CMD ["api.py"]

EXPOSE 5000