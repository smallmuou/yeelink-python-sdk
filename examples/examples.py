# -*- coding: utf-8 -*-

from yeelink import Yeelink
from yeelink.model import DataPointNumberModel

import time
import commands

client = Yeelink()
client.auth('bff018a9a85d0881ff016a1f7e6e53d0')


# Device API Examples
# devices = client.device.list()
# print devices

# device_id = client.device.create('Hello1111', 'H,a', 'Hello World', '111', 100.0, 200.0)
# print 'New Device:%s' % (device_id)

# client.device.edit(20801, '1212', '1111', '3333', '0000', 100.0, 100.0)

# client.device.delete(20810)

# Sensor API Examples
sensor_api = client.sensor(20748)

# sensor_id = sensor_api.create('switcher', 'Test11111111', 'Test Hello', 'Testtags', '开关', '布尔值')
# print sensor_id
#
# sensor_id = client.sensor.create(20748, 'value', 'Test11111111', 'Test Hello', 'Testtags', '开关', '布尔值')
# print sensor_id
# sensor_id = client.sensor.create(20748, 'gps', 'Test11111111', 'Test Hello', 'Testtags', '开关', '布尔值')
# print sensor_id
# sensor_id = client.sensor.create(20748, 'gen', 'Test11111111', 'Test Hello', 'Testtags', '开关', '布尔值')
# print sensor_id
# sensor_id = client.sensor.create(20748, 'photo', 'Test11111111', 'Test Hello', 'Testtags', '开关', '布尔值')
# print sensor_id



#sensors = sensor_api.list()
# print sensors

# sensor_api.delete(36482)
# sensor_api.delete(36483)
# sensor_api.delete(36484)
# sensor_api.delete(36485)
# sensor_api.delete(36486)
# sensor_api.delete(36487)
# sensor_api.delete(36488)

# sensor_api.detail(36523)

# DataPoint API Examples
datapoint_api = client.datapoint(20748, 36538)

i=0
while(i < 10):
    if datapoint_api.detail() == 1:
        print 'Music ON'
        a,b = commands.getstatusoutput('ls ~')
        print b
    else:
        print 'Music Off'
    i = i+1
    time.sleep(3)
#
# #datapoint_api.create(DataPointNumberModel(1))
#
# datapoint_api.edit()