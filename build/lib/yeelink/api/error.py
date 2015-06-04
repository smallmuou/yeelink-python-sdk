# -*- coding: utf-8 -*-

class YeelinkAPIError(Exception):
    def __init__(self, result):
        self.result = result
        try:
            self.type = result.code()
        except:
            self.type = ""

        # OAuth 2.0 Draft 10
        try:
            self.message = result.read()
        except:
            self.message = result

        Exception.__init__(self, self.message)
