FROM ubuntu:bionic
RUN apt update &&\
apt upgrade -y
RUN apt install -y python3 python3-pip
RUN pip3 install slackclient==1.0.6 \
pyyaml \
certifi==2019.6.16 \
chardet==3.0.4 \
requests==2.22.0 \
six==1.10.0 \
urllib3==1.25.3 \
websocket-client==0.44.0
WORKDIR /opt/slackbot/
COPY . /opt/slackbot
CMD python3 main.py
