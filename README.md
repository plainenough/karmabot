# Rebuilding a Karma Bot with Python and the Slack API:

![Load Commander](https://upload.wikimedia.org/wikipedia/en/f/f4/PinkyandtheBrain.TheBrain.png)

[![BCH compliance](https://bettercodehub.com/edge/badge/plainenough/karmabot?branch=master)](https://bettercodehub.com/)

PyBites Article: [Building a Karma Bot with Python and the Slack API](https://pybit.es/slack-karma-bot.html)

Original Project: [pybytes/karmabot](https://github.com/pybites/karmabot)

# Setup:
## Service - Systemd
1. Setup user 
```useradd -d /opt/slackbot/ -r -s /usr/sbin/nologin -U slackbot```
2. Clone the repo to /opt/slackbot/
```
mkdir -p /opt/slackbot/
git clone https://github.com/plainenough/karmabot.git /opt/slackbot
chown -R slackbot:slackbot /opt/slackbot/
```
3. Create service file - Use the above pybit articticle to get a gist on the setup process.
```
vim /etc/systemd/system/slackbot.service
```
```
[Unit]
Description=Karma Bot Service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=slackbot
Environment=SLACK_KARMA_TOKEN=<INSERT YOUR APP TOKEN HERE>
Environment=SLACK_KARMA_BOTUSER=<INSERT BOT NAME HERE>
WorkingDirectory=/opt/slackbot/
ExecStart=/usr/bin/python3 /opt/slackbot/main.py

[Install]
WantedBy=multi-user.target
```
```
systemctl enable slackbot.service
systemctl start slackbot.service
```
4. Add the botname to a your config file.

5. Generating a config file  will happen automatically when you start the service. But in case you want to just generate a config. \
I made a utility for that.
```
python3 utils/create_config.py
```

## Docker
### Building your own image. 
```
docker build -t karmabot -f ./container/Dockerfile .
```
### Running the container
* You need to make sure you generate a config file in the mounted directory.
```
docker run -v /PATH/TO/DATA:/opt/slackbot/data --name karmabot karmabot
```


# Other Information:
## Adding new commands.
1. Review commands/template.py (this is a great started template)
2. After coding your command, add an import to the bot/slack.py
```
from commands.newmodule import your_function
```
3. Add your command to the config and restart your service.


## TODO:
* Generate a working testing platform.
