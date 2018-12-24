# coding:utf-8
"""
bot config
"""
import os
import logging

DEBUG = bool(os.environ.get('debug', True))

LOG_LEVEL = os.environ.get("log_level") or logging.INFO

WEBHOOK_URL = os.environ.get('webhook_url')

WEBHOOK_PORT = os.environ.get('webhook_port')

SENTRY_URL = os.environ.get('sentry')

TOKEN = os.environ.get('token')
