# -*- coding: utf-8 -*-

from yeelink import Yeelink

client = Yeelink()
client.auth('bff018a9a85d0881ff016a1f7e6e53d0')

devices = client.device.list()
print devices