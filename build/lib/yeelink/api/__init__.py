# -*- coding: utf-8 -*-

from .device import Device, DeviceModel
from .sensor import Sensor, SensorModel
from .datapoint import DataPoint

class YeelinkAPI(object):

    def __repr__(self):
        return '<Yeelink API>'

    @property
    def device(self):
        return Device(self.version, self.apikey)

    def sensor(self, device_id):
        sen = Sensor(self.version, self.apikey)
        sen.device_id = device_id
        return sen

    def datapoint(self, device_id, sensor_id):
        dp = DataPoint(self.version, self.apikey)
        dp.device_id = device_id
        dp.sensor_id = sensor_id
        return dp
