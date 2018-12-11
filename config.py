#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
bot config
"""
import logging
import os

TOKEN = os.environ.get('token') or ''

LOG_LEVEL = os.environ.get('log_level') or logging.INFO

WEBHOOK_URL = os.environ.get('WEBHOOK_URL') or ""

WEBHOOK_PORT = int(os.environ.get('PORT', '8443'))
