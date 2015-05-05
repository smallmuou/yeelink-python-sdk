# -*- coding: utf-8 -*-

from yeelink import Yeelink

client = Yeelink()
client.auth('bff018a9a85d0881ff016a1f7e6e53d0')


# Device API Examples
devices = client.device.list()
print devices

# device_id = client.device.create('Hello1111', 'H,a', 'Hello World', '111', 100.0, 200.0)
# print 'New Device:%s' % (device_id)

# client.device.edit(20801, '1212', '1111', '3333', '0000', 100.0, 100.0)

# client.device.delete(20810)

# Sensor API Examples
# sensor_id = client.sensor.create(20748, 'switcher', 'Test11111111', 'Test Hello', 'Testtags', '开关', '布尔值')
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



sensors = client.sensor.list(20748)
print sensors

#client.sensor.delete(20748, 36477)

client.sensor.detail(20748, 36489)
