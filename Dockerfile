FROM ubuntu:latest
MAINTAINER Adam Horrigan "adhorrig@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ADD start.sh /app
CMD ["/app/start.sh"]