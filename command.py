#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
command file
"""
from tool import command_wrap

@command_wrap()
def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm a bot, please talk to me!")


