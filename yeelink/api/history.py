# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase

class History(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI History>'

    def list(self, start, end, interval, page):
        url = '/device/%d/sensor/%d.json?start=%s&end=%s&interval=%d&page=%d'%(self.device_id, self.sensor_id, start, end, interval, page)
        return self._get(url)