# -*- coding: utf-8 -*-

from .device import Device, DeviceModel
from .sensor import Sensor, SensorModel

class YeelinkAPI(object):

    def __repr__(self):
        return '<Yeelink API>'

    @property
    def device(self):
        return Device(self.version, self.apikey)

    @property
    def sensor(self):
        return Sensor(self.version, self.apikey)
