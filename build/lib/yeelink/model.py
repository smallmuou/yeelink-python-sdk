# -*- coding: utf-8 -*-

import time

class DataPointBaseModel(object):
    def __repr__(self):
        return '<DataPointBaseModel>'

class DataPointNumberModel(DataPointBaseModel):
    def __init__(self, value, timestamp = 0):
        if timestamp == 0:
            self.timestamp = time.time()
        else:
            self.timestamp = timestamp

        self.value = value

    def json_data(self):
        timestr = ''
        if isinstance(self.timestamp, float):
            x = time.localtime(self.timestamp)
            timestr = time.strftime('%Y-%m-%dT%H:%M:%S')
        else:
            timestr = self.timestamp
        return '{"timestamp":"%s", "value":%d}'%(timestr, self.value)

class DataPointGPSModel(DataPointBaseModel):
    def __init__(self, latitude, longitude, speed, offset=True, timestamp = 0):
        if timestamp == 0:
            self.timestamp = time.time()
        else:
            self.timestamp = timestamp

        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.offset = offset

    def json_data(self):
        x = time.localtime(self.timestamp)
        timestr = time.strftime('%Y-%M-%dT%h:%m:%s')
        return '{"timestamp":"%s", "value":{"lat":%f, "lng":%f, "speed":%f}}'%(timestr, self.latitude, self.longitude, self.speed)


class DataPointGenericsModel(DataPointBaseModel):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def json_data(self):
        return '{"key":"%s", "value":%s}' %(self.key, self.value)