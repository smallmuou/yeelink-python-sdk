# -*- coding: utf-8 -*-

from yeelink import Yeelink

client = Yeelink()
client.auth('bff018a9a85d0881ff016a1f7e6e53d0')

# devices = client.device.list()
# print devices

#device_id = client.device.create('Hello1111', 'H,a', 'Hello World', '111', 100.0, 200.0)
#print 'New Device:%s' % (device_id)

client.device.update(20790, '智能控制中心', '1111', '实现音乐、视频控制', '福州 福州市', 100.0, 100.0)