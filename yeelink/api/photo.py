# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase

class Photo(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI Photo>'

    def create(self, binary):
        url = '/device/%d/sensor/%d/photos'%(self.device_id, self.sensor_id)
        return self._post_original(url, binary)

    def info(self, key):
        url = '/device/%d/sensor/%d/photo/info/%s'%(self.device_id, self.sensor_id, key)
        return self._get(url)

    def content(self, key=''):
        url = '/device/%d/sensor/%d/photo/content/%s'%(self.device_id, self.sensor_id, key)
        return self._get(url)