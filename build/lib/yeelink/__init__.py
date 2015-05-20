# -*- coding: utf-8 -*-

from .yeelink import Yeelink

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SensorTypeValue     = 'value'
SensorTypeSwitcher  = 'switcher'
SensorTypeGPS       = 'gps'
SensorTypeGEN       = 'gen'
SensorTypePhoto     = 'photo'

__version__ = '1.1'
