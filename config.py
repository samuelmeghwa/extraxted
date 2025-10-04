#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8202713753:AAFGbXLUl7dxN1rILLXXepEVORgQFOVCsto")
    API_ID = int(os.environ.get("API_ID", "26653416"))
    API_HASH = os.environ.get("API_HASH", "37e7e14a87f5dcf3b654c9cbed9a87f5")
    AUTH_USERS = "1411895712"


