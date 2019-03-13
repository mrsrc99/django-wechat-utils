

django-wechat-utils
====================
* v0.0.1
* 基于python/django/rest-framework/sqlsite
* flask框架下也有同样功能的第三方库: flask-wechat-utils

quickstart
--------------------

1、安装模块
```shell
pip install django-wechat-utils
```

2、创建项目-mysite
```shell
django-admin startproject mysite
```

3、配置-mysite/mysite/settings.py
```python

ALLOWED_HOSTS = [
    ...,

    '127.0.0.1',
]

INSTALLED_APPS = [
	...,

    'rest_framework',
    'django_wechat_utils.wxuser.apps.WxuserConfig',
]

REST_FRAMEWORK = {
	...,

    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.AllowAny',
    ),
}

WXAPP_ID = 'xxx'
WXAPP_SECRET = 'xxx'
TOKEN_SECRET_KEY = 'xxx'
TOKEN_SALT = 'xxx'
TOKEN_TIMEOUT_HOURS = 24 * 365
TOKEN_FIELDS_REQUIRED = ['openid']
TOKEN_HEADER_FIELD = 'token'
LOGIN_CODE_FIELD_NAME = 'code'
UPDATE_IV_FIELD_NAME = 'iv'
UPDATE_ENCRYPTEDDATA_FIELD_NAME = 'encryptedData'
```

4、设置数据库
```shell
python manage.py migrate
```

5、启动服务
```shell
python manage.py runserver
```

提示
--------------------
* 接口文档页面: http://127.0.0.1:8000
* 管理后台页面: http://127.0.0.1:8000/admin
* 注意：登录管理后台之前需要创建超级管理员(老司机忽略),步骤:
```shell
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: *********
Password(again): *********
Superuser created successfully.
```

管理员界面效果
--------------------
* 登录页面:   ![file-list](https://dogbelt.cn/static/wyy/django-admin-login.jpg)
* 管理首页: ![file-list](https://dogbelt.cn/static/wyy/django-admin-index.jpg)
* 接口页面: ![file-list](https://dogbelt.cn/static/wyy/django-api-index.jpg)


接口使用
--------------------
* login
```python
import requests
url = 'http:127.0.0.1:8000/wxuser/'
headers = {
	'Content-Type':'application/json',
}
data = {
	'code':'xxx',
}
response = requests.post(url,headers=headers,json=data)
print response.json() #token
```

* auth
```python
import requests
url = 'http:127.0.0.1:8000/wxuser/'
headers = {
	'Content-Type':'application/json',
	'token':'xxx',
}
response = requests.get(url,headers=headers)
print response.json()
```

* register
```python
import requests
url = 'http:127.0.0.1:8000/wxuser/'
headers = {
	'Content-Type':'application/json',
	'token':'xxx',
}
data = {

	#使用这些字段
	'nickname':'xxx',
	'avatar':'xxx',
	'gender':'xxx',
	'city':'xxx',
	'province':'xxx',
	'country':'xxx',
	'language':'xxx',

	#或使用这两个字段
	'encryptedData':'xxx',
	'iv':'xxx',
}
response = requests.put(url,headers=headers,json=data)
print response.json()
```