# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import WXUser

# class WXUserInline(admin.TabularInline):

# 	model = WXUser
# 	extra = 1

class WXUserAdmin(admin.ModelAdmin):
	# fieldsets = [
	# 	(None,					{'fields':['nickname']}),
	# 	('Date information', 	{'fields':['last_ping_ts'], 'classes':['collapse']}),
	# ]

	#add inlines
	#inlines = [WXUserInline]

	#add list_display
	list_display = ('nickname','avatar_show','openid')

	#add list_filter
	list_filter = [
		'openid',
		'unionid',
		'wxid',
		'nickname',
		'avatar',
		'gender',
		'city',
		'province',
		'country',
		'language',
		'session_key',
		'mobile',
		'last_login_ts',
		'last_ping_ts',
		'created_ts',
		'status',
	]

	#add search_fields
	search_fields = ['nickname','mobile','openid','unionid']


admin.site.register(WXUser,WXUserAdmin)
