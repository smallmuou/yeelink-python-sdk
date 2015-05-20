# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase

class Photo(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI Photo>'

    def create_from_path(self, path):
        file = open(path, 'rb')
        # try:
        #     binary = file.read()
        # except Exception as err:
        #     print 'path not exist.'
        binary = file.read()
        file.close()
        return self.create(binary)

    def create(self, binary):
        url = '/device/%d/sensor/%d/photos'%(self.device_id, self.sensor_id)
        print url
        return self._post_original(url, binary)

    def info(self, key = ''):
        url = '/device/%d/sensor/%d/photo/info/%s'%(self.device_id, self.sensor_id, key)
        return self._get(url)

    def content(self, key=''):
        url = '/device/%d/sensor/%d/photo/content/%s'%(self.device_id, self.sensor_id, key)
        return self._get_original(url)

    def content_to_path(self, path, key=''):
        data = self.content(key)
        file = open(path, 'wb')
        file.write(data)
        file.close()