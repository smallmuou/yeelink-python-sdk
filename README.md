# yeelink-python-sdk

yeelink-python-sdk是根据[yeelink](http://www.yeelink.net/)提供的api v1.1文档写的python库，方便第三方开发者调用.

### 1.Install
* 下载源码
<pre>
git clone https://github.com/smallmuou/yeelink-python-sdk.git
</pre>

* 安装
<pre>
cd yeelink-python-sdk
sudo python setup.py install
</pre>

### 2. Usage
* 根据不同需求引入相应的内容
<pre>
from yeelink import Yeelink # 必须引入
from yeelink import SensorTypeValue, SensorTypeSwitcher, SensorTypePhoto, SensorTypeGEN, SensorTypeGPS # 传感器类型，当要创建传感器需要引入
from yeelink.model import DataPointNumberModel #数据点，需要用到数据点则需要引入
</pre>

* 创建client
<pre>
client = Yeelink()
client.auth('< your api key >')
</pre>
api key可以进入你的用户管理首页查看.

* 设备操作
<pre>
device_adapter = client.device()
# 创建
device_id = device_adapter.create('Test', 'Test tags', 'Test about', 'fujian', 100.0, 200.0)
# 编辑
device_adapter.edit(device_id, 'Test1', 'Test1 tags', 'Test1 about', 'fujian', 100.0, 100.0)
# 罗列
devices = device_adapter.list()
for device in devices:
    print 'id:'+ str(device.id) + ',title:'+ device.title
#  删除
device_adapter.delete(device_id)
</pre>

更多代码可以详见**examples.py**

### 3. License
该sdk采用MIT，各位可以随意使用.

### 4. Contribute
欢迎有兴趣的童鞋加入该项目的开发，可以采用fork并提交pull merge方式. 我会及时merge.

### 5. Contact
如果大家在使用此sdk过程中，有任何问题或意见可以通过email反馈给我，我会尽快处理，我的e-mail: lvyexuwenfa100@126.com


