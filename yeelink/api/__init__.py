# -*- coding: utf-8 -*-

from .device import Device, DeviceModel

class YeelinkAPI(object):

    def __repr__(self):
        return '<Yeelink API>'

    @property
    def device(self):
        return Device(self.version, self.apikey)
