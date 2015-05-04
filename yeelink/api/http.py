# -*- coding:utf-8 -*-

import urllib
import urllib2
import json

AUTHKEY = 'U-ApiKey'

def http_get(url, apikey):
    request = urllib2.Request(url)
    request.get_method = lambda:"GET"
    request.add_header(AUTHKEY, apikey)
    return urllib2.urlopen(request)

def http_put(url, apikey, data):
    jdata = json.dumps(data)
    request = urllib2.Request(url, jdata)
    request.get_method = lambda:"PUT"
    request.add_header(AUTHKEY, apikey)
    return urllib2.urlopen(request)

def http_post(url, apikey, data):
    jdata = json.dumps(data)
    request = urllib2.Request(url, jdata)
    request.get_method = lambda:"POST"
    request.add_header(AUTHKEY, apikey)
    return urllib2.urlopen(request)

def http_delete(url, apikey):
    request = urllib2.Request(url)
    request.get_method = lambda:"DELETE"
    request.add_header(AUTHKEY, apikey)
    return urllib2.urlopen(request)
