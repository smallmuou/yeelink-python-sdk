# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase
import json

class DeviceModel(object):
    def __init__(self, data):
        self.title = data['title']
        self.about = data['about']
        self.tags = data['tags']
        self.local = data['local']
        self.latitude = float(data['latitude'])
        self.longitude = float(data['longitude'])

    def __repr__(self):
        return '[id:%d title:%s, about:%s, tags:%s, local:%s, latitude:%f, longitude:%f]' % (self.id, self.title, self.about, self.tags, self.local, self.latitude, self.longitude)

class Device(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI Device>'

    def create(self, title, tags, about, location_locale, location_latitude, location_longitude):
        url = '/devices'
        data = '{"title":"%s", "about":"%s", "tags":"%s", "location":{"local":"%s", "latitude":%f, "longitude":%f}}' % (title, about, tags, location_locale, location_latitude, location_longitude)
        return int(self._post(url, data)['device_id'])

    def edit(self, device_id, title, tags, about, location_locale, location_latitude, location_longitude):
        url = '/device/%d' % (device_id)
        data = '{"title":"%s", "about":"%s", "tags":"%s", "location":{"local":"%s", "latitude":%f, "longitude":%f}}' % (title, about, tags, location_locale, location_latitude, location_longitude)
        return self._put(url, data)

    def list(self):
        url = '/devices'
        items = self._get(url)
        devices = []
        for item in items:
            device = DeviceModel(item)
            device.id = int(item['id'])
            devices.append(device)
        return devices

    def detail(self, device_id):
        url = '/device/%d' % (device_id)
        return DeviceModel(self._get(url))

    def delete(self, device_id):
        url = '/device/%d' % (device_id)
        return self._delete(url)
