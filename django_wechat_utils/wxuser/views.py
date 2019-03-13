# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# django
from django.conf import settings

# rest ramework
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# mine
from models import WXUser
from serializer import WXUserSerializer

# mine - wx
from utils import register
from utils import login
from utils import auth

class WXUserViewSet(viewsets.ModelViewSet):

	queryset = WXUser.objects.all()
	serializer_class = WXUserSerializer
	permission_class = (AllowAny,)

	def list(self, request, pk=None):
		return Response({'test':'test'}, status=status.HTTP_200_OK)

	@login
	def create(self, request, pk=None):
		return Response(
			{
				'nickname':request.wechat_user.nickname,
				'avatar':request.wechat_user.avatar,
				'token':request.wechat_user_token,
			}
		)

	@register
	def put(self, request, pk=None):
		return Response(
			{
				'nickname':request.wechat_user.nickname,
				'avatar':request.wechat_user.avatar,
			}
		)

	@auth
	def retrieve(self, request, pk=None):
		return Response(
			{
				'nickname':request.wechat_user.nickname,
				'avatar':request.wechat_user.avatar,
			}
		)

