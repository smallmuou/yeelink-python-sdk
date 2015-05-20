# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase
from .device import DeviceModel

class Product(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI Product>'

    def detail(self):
        url = '/product/%d'%(self.product_sn)
        item = self._get(url)
        device = DeviceModel(item)
        device.id = int(item['id'])
        return device

    def bind(self, user):
        url = '/product/bind/%d'%(self.product_sn)
        body = '{"user_login":%s, "force":true}'%(user)
        return self._post(url)

    def feed(self):
        url = '/product/feed/%d'%(self.product_sn)
        return self._post(url)['message']