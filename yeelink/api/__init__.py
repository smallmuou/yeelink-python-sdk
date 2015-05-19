# -*- coding: utf-8 -*-

from .device import Device, DeviceModel
from .sensor import Sensor, SensorModel
from .datapoint import DataPoint
from .photo import Photo
from .history import History
from .product import Product

class YeelinkAPI(object):

    def __repr__(self):
        return '<Yeelink API>'

    @property
    def device(self):
        return Device(self.version, self.apikey)

    def sensor(self, device_id):
        sen = Sensor(self.version, self.apikey)
        sen.device_id = device_id
        return sen

    def datapoint(self, device_id, sensor_id):
        dp = DataPoint(self.version, self.apikey)
        dp.device_id = device_id
        dp.sensor_id = sensor_id
        return dp

    def photo(self, device_id, sensor_id):
        ph = Photo(self.version, self.apikey)
        ph.device_id = device_id
        ph.sensor_id = sensor_id
        return ph

    def history(self, device_id, sensor_id):
        his = History(self.version, self.apikey)
        his.device_id = device_id
        his.sensor_id = sensor_id
        return his

    def product(self, product_sn):
        pro = Product(self.version, self.apikey)
        pro.product_sn = product_sn
        return pro
