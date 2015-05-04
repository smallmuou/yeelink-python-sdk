# -*- coding: utf-8 -*-

class YeelinkBaseError(Exception):
    def __str__(self):
        return "ERROR(%s): %s" % (self.code, self.reason)

class YeelinkAuthError(YeelinkBaseError):
    def __init__(self, code, reason):
        self.code = code
        self.reason = reason

class YeelinkAPIError(YeelinkBaseError):
    def __init__(self, response):
        self.code = response.code
        self.reason = response.reason