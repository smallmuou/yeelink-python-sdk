# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase
from yeelink.model import DataPointBaseModel


class DataPoint(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI DataPoint>'

    '''
    对于开关型传感器，只允许创建一次，否则会报DUPLICATE KEY错误
    '''
    def create(self, data):
        url = '/device/%d/sensor/%d/datapoints'%(self.device_id, self.sensor_id)
        if isinstance(data, list):
            body = '['
            for model in data:
                body = body + model.json_data() + ','
            if len(body) > 1:
                body = body[:-1]
            body = body + ']'
            return self._post(url, body)
        elif isinstance(data, DataPointBaseModel):
            return self._post(url, data.json_data())

    def edit(self, model):
        url = '/device/%d/sensor/%d/datapoint/%s'%(self.device_id, self.sensor_id, model.json_key())
        return self._put(url, '{"value":%s}'%(model.json_value()))

    def detail(self, key=''):
        url = '/device/%d/sensor/%d/datapoint/%s'%(self.device_id, self.sensor_id, key)
        return self._get(url)['value']

    def delete(self, key):
        url = '/device/%d/sensor/%d/datapoint/%s'%(self.device_id, self.sensor_id, key)
        return self._delete(url)