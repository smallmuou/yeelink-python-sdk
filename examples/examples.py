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

#print client.device.create('Hello1111', 'H,a', 'Hello World', '111', 100.0, 200.0)
# print 'New Device:%s' % (device_id)

# client.device.edit(20801, '1212', '1111', '3333', '0000', 100.0, 100.0)

# client.device.delete(20810)

# Sensor API Examples
sensor_api = client.sensor(21034)
#print sensor_api.create('value', 'value', 'Test Hello', 'Testtags', '开关', '布尔值')

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



print sensor_api.list()
# print sensors
#
# sensor_api.delete(36844)
# sensor_api.delete(36845)
# sensor_api.delete(36846)
# sensor_api.delete(36847)
# sensor_api.delete(36848)
# sensor_api.delete(36849)
# sensor_api.delete(36850)
# sensor_api.delete(36851)
# sensor_api.delete(36852)
# sensor_api.delete(36853)
# sensor_api.delete(36854)
# sensor_api.delete(36855)
# sensor_api.delete(36856)
# sensor_api.delete(36857)

# sensor_api.detail(36523)

# DataPoint API Examples
datapoint_api = client.datapoint(21034, 36869)
print datapoint_api.detail()

#datapoint_api.create(DataPointNumberModel(1000))
datapoint_api.create([DataPointNumberModel(77, '2015-05-09T12:10:23'), DataPointNumberModel(80, '2015-05-09T12:11:23')])
#
#datapoint_api.edit('2015-05-09T12:02:29')