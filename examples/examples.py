# -*- coding: utf-8 -*-

from yeelink import Yeelink
from yeelink import SensorTypeValue, SensorTypeSwitcher, SensorTypePhoto, SensorTypeGEN, SensorTypeGPS

client = Yeelink()
client.auth('bff018a9a85d0881ff016a1f7e6e53d0')


# Device API Examples
device_adapter = client.device()

#print device_adapter.create('Hello1111', 'H,a', 'Hello World', '111', 100.0, 200.0)

# device_adapter.edit(20801, '1212', '1111', '3333', '0000', 100.0, 100.0)

# device_adapter.delete(20810)

# Sensor API Examples
sensor_adapter = client.sensor(21034)
# print sensor_adapter.create(SensorTypeGPS, 'value', 'Test Hello', 'Testtags', '开关', '布尔值')

# sensor_id = sensor_adapter.create('switcher', 'Test11111111', 'Test Hello', 'Testtags', '开关', '布尔值')
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

#print sensor_adapter.list()
#
# sensor_adapter.delete(36844)

# sensor_adapter.detail(36523)

# DataPoint API Examples
#datapoint_api = client.datapoint(21034, 36869)
#print datapoint_api.detail()

#datapoint_api.create(DataPointNumberModel(1000))
#datapoint_api.create([DataPointNumberModel(77, '2015-05-09T12:10:23'), DataPointNumberModel(80, '2015-05-09T12:11:23')])
#
#datapoint_api.edit('2015-05-09T12:02:29')

# Photo
photo_adapter = client.photo(21034, 38080)
photo_adapter.create_from_path('/Users/starnet/Downloads/1.gif')
print photo_adapter.info()