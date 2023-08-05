# Simplest telegram bot
The simplest telegram bot out there that could be embedded into your apps as a notification service
and could listen for remote commands and executes them.

# Installation
```
pip install pytele
```

# Introduction
The telegram bot is under development right now and only the notification service workst them as environment variables respectively RECAPTCHA_SITE_KEY and RECAPTCHA_SECRET_KEY.

```
from telegram import Bot

bot = Bot() # takens the BOT's token from environment variables - TELEGRAM_BOT_TOKEN
bot.send_msg(to='chait_id', msg='your message')
```