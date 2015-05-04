# -*- coding: utf-8 -*-

from .api import YeelinkAPI

class Yeelink(YeelinkAPI):
    def __init__(self):
        self.version = 'v1.1'

    def __repr__(self):
        return '<Yeelink Client>'

    def auth(self, apikey):
        self.apikey = apikey


