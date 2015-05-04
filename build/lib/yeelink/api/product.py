from .device import Device
from .sensor import Sensor
from .datapoint import DataPoint
from .photo import Photo
from .history import History
from .product import Product

class YeelinkAPI(object):
    def __repr__(self):
        return '<Yeelink API>'

    @property
    def device(self):
        return Device(self.apikey)

    @property
    def sensor(self):
        return Sensor(self.apikey)

    @property
    def datapoint(self):
        return Datapoint(self.apikey)

    @property
    def photo(self):
        return Photo(self.apikey)

    @property
    def history(self):
        return History(self.apikey)

    @property
    def product(self):
        return Product(self.apikey)