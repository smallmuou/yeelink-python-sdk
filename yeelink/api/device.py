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
        url = '/%s/devices' % (self.version)
        data = '{"title":"%s", "about":"%s", "tags":"%s", "location":{"local":"%s", "latitude":%f, "longitude":%f}}' % (title, about, tags, location_locale, location_latitude, location_longitude)
        jdata = json.loads(data)
        return self._post(url, jdata)['device_id']

    def update(self, device_id, title, tags, about, location_locale, location_latitude, location_longitude):
        url = '/%s/device/%d' % (self.version, device_id)
        data = '{"title":"%s", "about":"%s", "tags":"%s", "location":{"local":"%s", "latitude":%f, "longitude":%f}}' % (title, about, tags, location_locale, location_latitude, location_longitude)
        jdata = json.loads(data)
        return self._put(url, jdata)

    def list(self):
        url = '/%s/devices' % (self.version)
        items = self._get(url)
        devices = []
        for item in items:
            device = DeviceModel(item)
            device.id = int(item['id'])
            devices.append(device)
        return devices

    def get(self, device_id):
        url = '/%s/device/%d' % (self.version, device_id)
        return DeviceModel(self._get(url))

    def delete(self, device_id):
        url = '/%s/devices/%d' % (self.version, device_id)
        return self._delete(url)
