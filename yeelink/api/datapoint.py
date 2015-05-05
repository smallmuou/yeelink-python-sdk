# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase

class DataPoint(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI DataPoint>'

    '''
    对于开关型传感器，只允许创建一次，否则会报DUPLICATE KEY错误
    '''
    def create(self, model):
        url = '/device/%d/sensor/%d/datapoints'%(self.device_id, self.sensor_id)
        return self._post(url, model.json_data())

    def edit(self):
        url = '/device/%d/sensor/%d/datapoint'%(self.device_id, self.sensor_id)
        return self._put(url, '{"value":1}')


    def detail(self, key=''):
        url = '/device/%d/sensor/%d/datapoint/%s'%(self.device_id, self.sensor_id, key)
        return self._get(url)['value']

