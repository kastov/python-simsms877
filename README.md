# smshub-org


### Описание на русском ниже

Wrapper for automatic reception of SMS-messages by smshub.org

[![N|Solid](https://img.shields.io/pypi/pyversions/smsactivateru.svg)](https://pypi.python.org/pypi/smsactivateru)

### Installation
You can install or upgrade package with:
```
$ pip install smshuborg --upgrade
```
Or you can install from source with:
```
$ git clone https://github.com/ravensoracle/python-smshub-org
$ cd python-smshub-org
$ python setup.py install
```
...or install from source buth with pip
```
$ pip install git+https://github.com/ravensoracle/python-smshub-org
```
### Example
```python
from smshuborg import Sms, SmsService, GetNumber

wrapper = Sms('API KEY')

activation = GetNumber(
	service=SmsService().Youla,
).request(wrapper)

input('Press enter if you sms was sent')

activation.was_sent().request(wrapper)
code = activation.wait_code(wrapper=wrapper)
print(code)
```
More examples located in /example/ dir

----
Библиотека на python для работы с api сервиса автоматического приёма смс – smshub.org

[![N|Solid](https://img.shields.io/pypi/pyversions/smsactivateru.svg)](https://pypi.python.org/pypi/smsactivateru)

### Установка
Установка с помощью стандартного пакетного менеджера pip:
```
$ pip install smshuborg --upgrade
```
Либо установка напрямую из репозитория, с ручной сборкой
```
$ git clone https://github.com/ravensoracle/python-smshub-org
$ cd python-smshub-org
$ python setup.py install
```
...либо установка через pip но из репозитория, минуя сервера pypi
```
$ pip install git+https://github.com/ravensoracle/python-smshub-org
```
### Простой пример
```python
from smshuborg import Sms, SmsService, GetNumber

wrapper = Sms('API KEY')

activation = GetNumber(
	service=SmsService().Youla,
).request(wrapper)

input('Press enter if you sms was sent')

activation.was_sent().request(wrapper)
code = activation.wait_code(wrapper=wrapper)
print(code)
```
Это пример использует встроенный обработчик. Вы можете вручную устанавливать статусы и управлять процессом, а так же много чего ещё.
Больше примеров находится в папке /example/
