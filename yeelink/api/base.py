# -*- coding: utf-8 -*-

from .error import YeelinkAuthError, YeelinkAPIError
from .http import http_get, http_delete, http_post, http_put
import json

BASEURL='http://api.yeelink.net'

def check_execption(func):
    def _check(*arg, **kws):
        response = func(*arg, **kws)
        if response.code >= 400:
            if response.code == 403:
                raise YeelinkAuthError(401, 'UNAUTHORIZED')
            else:
                raise YeelinkAPIError(response)
        body = response.read()
        if body:
            return json.loads(body)
        return body

    return _check

class YeelinkAPIBase(object):

    def __init__(self, apiversion, apikey):
        self.version = apiversion
        self.apikey = apikey
        if self.apikey == "":
            raise YeelinkAuthError(401, 'UNAUTHORIZED')

    def __repr__(self):
        return '<YeelinkAPI Base>'

    @check_execption
    def _get(self, url, **opts):
        url = BASEURL+url
        return http_get(url, self.apikey, **opts)

    @check_execption
    def _post(self, url, **opts):
        url = BASEURL+url
        return http_post(url, self.apikey, **opts)

    @check_execption
    def _put(self, url, **opts):
        url = BASEURL+url
        return http_put(url, self.apikey, **opts)

    @check_execption
    def _delete(self, url, **opts):
        url = BASEURL+url
        return http_delete(url, self.apikey, **opts)
