# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.html import format_html

import time
def now_ts():
	return int(time.time())

# Create your models here.

class WXUser(models.Model):

	openid = models.CharField(max_length=200)
	unionid = models.CharField(max_length=200,default='')
	wxid = models.CharField(max_length=200,default='')
	nickname = models.CharField(max_length=200,default='')
	avatar = models.CharField(max_length=200,default='')
	gender = models.IntegerField(default=0)
	city = models.CharField(max_length=200,default='')
	province = models.CharField(max_length=200,default='')
	country = models.CharField(max_length=200,default='')
	language = models.CharField(max_length=200,default='')

	session_key = models.CharField(max_length=200,default='')
	mobile = models.CharField(max_length=200,default='')

	last_login_ts = models.IntegerField(default=now_ts())
	last_ping_ts = models.IntegerField(default=now_ts())

	status = models.IntegerField(default=1)
	created_ts = models.IntegerField(default=now_ts())


	#image
	def avatar_show(self):
		return format_html(
			'<img src="{}" width="40px"/>',
			self.avatar,
		)
	avatar_show.short_description = u'头像'

