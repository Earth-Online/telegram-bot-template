#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
tool module
"""
import logging
from telegram.ext import CommandHandler


def command_wrap(name: str = "", pass_chat_data=False,
                 pass_user_data=False, pass_args=False, **kwargs):
    """
    wrap command handle
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = None
            logging.debug(f"call {func.__name__} ")
            try:
                ret = func(*args, **kwargs)
            except Exception as error:
                logging.error(error)
            return ret

        return CommandHandler(
            name or func.__name__, pass_chat_data=pass_chat_data,
            pass_user_data=pass_user_data, pass_args=pass_args,
            callback=wrapper, **kwargs)

    return decorator
