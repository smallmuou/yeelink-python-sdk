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
        return '{"timestamp":"%s", "value":%d}'%(self.json_key(), self.json_value())

    def json_key(self):
        timestr = ''
        if isinstance(self.timestamp, float):
            x = time.localtime(self.timestamp)
            timestr = time.strftime('%Y-%m-%dT%H:%M:%S')
        else:
            timestr = self.timestamp
        return timestr

    def json_value(self):
        return self.value

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
        return '{"timestamp":"%s", "value":%s}'%(self.json_key(), self.json_value())

    def json_key(self):
        x = time.localtime(self.timestamp)
        return time.strftime('%Y-%M-%dT%h:%m:%s')

    def json_value(self):
        return '{"lat":%f, "lng":%f, "speed":%f}'%(self.latitude, self.longitude, self.speed)

class DataPointGenericsModel(DataPointBaseModel):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def json_data(self):
        return '{"key":"%s", "value":%s}' %(self.json_key(), self.json_value())

    def json_key(self):
        return self.key

    def json_value(self):
        return self.value