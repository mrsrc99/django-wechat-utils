#coding:utf8
from django.conf import settings

WXAPP_ID = 'xxx' if hasattr(settings,'WXAPP_ID') == False else settings.WXAPP_ID
WXAPP_SECRET = 'xxx' if hasattr(settings,'WXAPP_SECRET') == False else settings.WXAPP_SECRET

TOKEN_SECRET_KEY = 'xxx' if hasattr(settings,'TOKEN_SECRET_KEY') == False else settings.TOKEN_SECRET_KEY
TOKEN_SALT = 'xxx' if hasattr(settings,'TOKEN_SALT') == False else settings.TOKEN_SALT
TOKEN_TIMEOUT_HOURS = 24 * 365 if hasattr(settings,'TOKEN_TIMEOUT_HOURS') == False else settings.TOKEN_TIMEOUT_HOURS
TOKEN_FIELDS_REQUIRED = ['openid'] if hasattr(settings,'TOKEN_FIELDS_REQUIRED') == False else settings.TOKEN_FIELDS_REQUIRED

TOKEN_HEADER_FIELD = 'token' if hasattr(settings,'TOKEN_HEADER_FIELD') == False else settings.TOKEN_HEADER_FIELD
LOGIN_CODE_FIELD_NAME = 'code' if hasattr(settings,'LOGIN_CODE_FIELD_NAME') == False else settings.LOGIN_CODE_FIELD_NAME
UPDATE_IV_FIELD_NAME = 'iv' if hasattr(settings,'UPDATE_IV_FIELD_NAME') == False else settings.UPDATE_IV_FIELD_NAME
UPDATE_ENCRYPTEDDATA_FIELD_NAME = 'encryptedData' if hasattr(settings,'UPDATE_ENCRYPTEDDATA_FIELD_NAME') == False else settings.UPDATE_ENCRYPTEDDATA_FIELD_NAME
