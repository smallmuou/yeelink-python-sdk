# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase

class SensorModel(object):
    def __init__(self, data):
        self.type = int(data['type'])
        self.title = data['title']
        self.about = data['about']
        self.last_update = data['last_update']
        self.last_data = data['last_update']
        self.last_data_gen = data['last_update']

    def __repr__(self):
        return '[id:%d, title:%s, type:%d, about:%s, last_update:%s]'%(self.id, self.title, self.type, self.about, self.last_update)

class Sensor(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI Sensor>'

    def create(self, type, title, about, tags, unit_name, unit_symbol):
        url = '/device/%d/sensors'%(self.device_id)
        data = '{"type":"%s", "title":"%s", "about":"%s", "tags":"%s", "unit":{"name":"%s", "symbol":"%s"}}' % (type, title, about, tags, unit_name, unit_symbol)
        return int(self._post(url, data)['sensor_id'])

    def edit(self, sensor_id, title, about, tags, unit_name, unit_symbol):
        url = '/device/%d/sensor/%d'%(self.device_id, sensor_id)
        data = '{"title":"%s", "about":"%s", "tags":"%s", "unit":{"name":"%s", "symbol":"%s"}}' % (title, about, tags, unit_name, unit_symbol)
        return self._put(url, data)

    def list(self):
        url = '/device/%d/sensors'%(self.device_id)
        items = self._get(url)
        sensors = []
        for item in items:
            sensor = SensorModel(item)
            sensor.id = int(item['id'])
            sensors.append(sensor)
        return sensors

    def detail(self, sensor_id):
        url = '/device/%d/sensor/%d'%(self.device_id, sensor_id)
        return self._get(url)

    def delete(self, sensor_id):
        url = '/device/%d/sensor/%d'%(self.device_id, sensor_id)
        return self._delete(url)
