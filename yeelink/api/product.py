# -*- coding: utf-8 -*-

from .base import YeelinkAPIBase

class Product(YeelinkAPIBase):
    def __repr__(self):
        return '<YeelinkAPI Product>'

    def detail(self):
        url = '/product/%d'%(self.product_sn)
        return self._get(url)

    def bind(self):
        url = '/product/bind/%d'%(self.product_sn)
        return self._post(url)

    def feed(self):
        url = '/product/feed/%d'%(self.product_sn)
        return self._post(url)