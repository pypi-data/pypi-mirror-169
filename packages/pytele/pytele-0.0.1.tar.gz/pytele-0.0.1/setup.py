# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['telegram']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pytele',
    'version': '0.0.1',
    'description': '',
    'long_description': "# Simplest telegram bot\nThe simplest telegram bot out there that could be embedded into your apps as a notification service\nand could listen for remote commands and executes them.\n\n# Installation\n```\npip install pytele\n```\n\n# Introduction\nThe telegram bot is under development right now and only the notification service workst them as environment variables respectively RECAPTCHA_SITE_KEY and RECAPTCHA_SECRET_KEY.\n\n```\nfrom telegram import Bot\n\nbot = Bot() # takens the BOT's token from environment variables - TELEGRAM_BOT_TOKEN\nbot.send_msg(to='chait_id', msg='your message')\n```",
    'author': 'Jordan Raychev',
    'author_email': 'jpraychev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
