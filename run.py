#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
run bot
"""
import logging
from telegram.ext import Updater
import config
from command import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=config.LOG_LEVEL)


def main():
    """
    run bot
    """
    updater = Updater(token=config.TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start)
    logging.info("bot run start ")
    if not config.WEBHOOK_URL:
        updater.start_polling()
    else:
        updater.start_webhook(listen="0.0.0.0",
                              port=config.WEBHOOK_PORT,
                              url_path=config.TOKEN)
        updater.bot.set_webhook(config.WEBHOOK_URL + config.TOKEN)
    updater.idle()
