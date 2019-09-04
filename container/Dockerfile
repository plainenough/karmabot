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
CMD python3 main.py && tail -f /opt/slackbot/data/slackbot.log
LABEL     org.label-schema.name="Karmabot" \
          org.label-schema.description="Hipchat like Karma bot for slack." \
          org.label-schema.url="https://github.com/plainenough/karmabot.git" \
          org.label-schema.vendor="Tosstalk.com" \
          org.label-schema.version=$version
