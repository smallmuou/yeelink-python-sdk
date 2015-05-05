# -*- coding: utf-8 -*-

from .error import YeelinkAuthError, YeelinkAPIError
from .http import http_get, http_delete, http_post, http_put
import json

BASEURL='http://api.yeelink.net'

def check_execption(func):
    def _check(*arg, **kws):
        try:
            response = func(*arg, **kws)
            if response.code < 400:
                body = response.read()
                if body:
                    return json.loads(body)
                return body
        except Exception as err:
            print YeelinkAPIError(err)

    return _check

class YeelinkAPIBase(object):

    def __init__(self, apiversion, apikey):
        self.version = apiversion
        self.apikey = apikey
        self.baseurl = BASEURL+'/'+self.version
        if self.apikey == "":
            raise YeelinkAuthError(401, 'UNAUTHORIZED')

    def __repr__(self):
        return '<YeelinkAPI Base>'

    @check_execption
    def _get(self, url):
        url = self.baseurl+url
        return http_get(url, self.apikey)

    @check_execption
    def _post(self, url, data):
        url = self.baseurl+url
        return http_post(url, self.apikey, json.loads(data))

    @check_execption
    def _put(self, url, data):
        url = self.baseurl+url
        return http_put(url, self.apikey, json.loads(data))

    @check_execption
    def _delete(self, url):
        url = self.baseurl+url
        return http_delete(url, self.apikey)
