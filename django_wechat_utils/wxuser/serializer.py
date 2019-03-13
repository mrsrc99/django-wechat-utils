#coding:utf8

# rest
from rest_framework import serializers

# my model
from models import WXUser


class WXUserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = WXUser
		fields = ('openid','nickname','avatar','gender','city','province','country','language')
