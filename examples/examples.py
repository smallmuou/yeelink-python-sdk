# -*- coding: utf-8 -*-

from yeelink import Yeelink, SensorTypeValue, SensorTypeSwitcher, SensorTypePhoto, SensorTypeGEN, SensorTypeGPS
from yeelink.model import DataPointNumberModel

client = Yeelink()
client.auth('<your api key>')

##############################
#            设备             #
##############################
device_adapter = client.device()

# 创建设备
device_id = device_adapter.create('Test', 'Test tags', 'Test about', 'fujian', 100.0, 200.0)
print "创建的设备id:"+str(device_id)

# 编辑设备
device_adapter.edit(device_id, 'Test1', 'Test1 tags', 'Test1 about', 'fujian', 100.0, 100.0)

# 罗列设备, 返回DeviceModel列表, 详见device.py
devices = device_adapter.list()
for device in devices:
    print 'id:'+ str(device.id) + ',title:'+ device.title

# 删除设备
device_adapter.delete(device_id)

##############################
#          传感器             #
##############################
sensor_adapter = client.sensor(device_id)

# 创建传感器
sensor_id = sensor_adapter.create(SensorTypeValue, 'Test', 'Test about', 'Test tag', '开关', '布尔值')

# 编辑传感器
sensor_adapter.edit(sensor_id, 'Test1', 'Test1 about', 'Test1 tag', '数值', '米')

# 罗列传感器, 返回SensorModel，详见sensor.py
sensors = sensor_adapter.list()
for sensor in sensors:
    print sensor

# 查看详情
sensor_adapter.detail(sensor_id)

# 删除传感器
sensor_adapter.delete(sensor_id)

##############################
#           数据              #
##############################
datapoint_adapter = client.datapoint(device_id, sensor_id)

# 创建数据点
datapoint_adapter.create(DataPointNumberModel(1000))

# 编辑数据点
datapoint_adapter.edit('2015-05-09T12:02:29')

##############################
#            照片             #
##############################
photo_adapter = client.photo(device_id, sensor_id)

# 上传图片
photo_adapter.create_from_path('/Users/starnet/Downloads/1.gif')

# 图片信息
print photo_adapter.info()