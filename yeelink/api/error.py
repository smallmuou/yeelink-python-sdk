# -*- coding: utf-8 -*-

class YeelinkBaseError(Exception):
    def __str__(self):
        return "***%s (%s)*** %s" % (self.status, self.reason, self.msg)

class YeelinkAuthError(YeelinkBaseError):
    def __init__(self, status, reason, message={}):
        self.status = status
        self.reason = reason
        self.message = message

class YeelinkAPIError(YeelinkBaseError):
    def __init__(self, response):
        self.status = response.status
        self.reason = response.reason
        self.message = response.parsed