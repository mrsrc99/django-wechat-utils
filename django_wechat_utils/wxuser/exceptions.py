#coding:utf8
import json


#error 						  	登录10:01错误位置
ERROR_TOKEN_MISSING 			= 1001
ERROR_TOKEN_WRONG_DECRYPT		= 1002
ERROR_TOKEN_TIMEOUT				= 1003
ERROR_TOKEN_WRONG_FIELDS		= 1004
ERROR_TOKEN_WRONG_NO_USER		= 1005
ERROR_CODE_WRONG				= 1006
ERROR_IV_ENCRYPTED_WRONG 		= 1007
ERROR_MONGO_GET_USER_WRONG		= 1008
ERROR_TOKEN_WRONG_ENCRYPT		= 1009
ERROR_CONTENT_TYPE_NOT_JSON		= 1010

ERROR_LOGIN_CODE_MISSING				= 1101
ERROR_LOGIN_CODE_FREQUENCY_LIMIT		= 1102
ERROR_LOGIN_CODE_WEIXIN_BUSY			= 1103
ERROR_LOGIN_CODE_LOST_EFFECT			= 1104
ERROR_LOGIN_CODE_NO_WHY					= 1105
ERROR_LOGIN_MONGO_CREATE_FAIL			= 1106
ERROR_LOGIN_MONGO_UPDATE_FAIL			= 1107
ERROR_REGISTER_MISSING_IV_OR_ENCRYPTED	= 1108
ERROR_REGISTER_MISSING_TOKEN			= 1109
ERROR_REGISTER_NO_USER					= 1110

ERROR_MISSING_WXAPP_ID				= 1200
ERROR_MISSING_WXAPP_SECRET			= 1201

ERROR_CONFIG_WEB_NAME_WRONG								= 1202
ERROR_CONFIG_TOKEN_SECRET_KEY_WRONG						= 1203
ERROR_CONFIG_TOKEN_TIMEOUT_HOURS_WRONG					= 1204
ERROR_CONFIG_TOKEN_SALT_WRONG							= 1205
ERROR_CONFIG_TOKEN_FIELDS_REQUIRED_WRONG				= 1206
ERROR_CONFIG_TOKEN_HEADER_FIELD_WRONG					= 1207
ERROR_CONFIG_LOGIN_CODE_FIELD_NAME_WRONG				= 1208
ERROR_CONFIG_UPDATE_IV_FIELD_NAME_WRONG					= 1209
ERROR_CONFIG_UPDATE_ENCRYPTEDDATA_FIELD_NAME_WRONG		= 1210



ERRORS = {
	ERROR_TOKEN_MISSING:{
		'code':ERROR_TOKEN_MISSING,
		'message': 'missing token',
		'category':None,
	},

	ERROR_TOKEN_WRONG_DECRYPT:{
		'code':ERROR_TOKEN_WRONG_DECRYPT,
		'message':'decrypt error, wrong token',
		'category':None,
	},

	ERROR_TOKEN_TIMEOUT:{
		'code':ERROR_TOKEN_TIMEOUT,
		'message':'token overdue',
		'category':None,
	},

	ERROR_TOKEN_WRONG_FIELDS:{
		'code':ERROR_TOKEN_WRONG_FIELDS,
		'message':'token wrong fields',
		'category':None,
	},

	ERROR_TOKEN_WRONG_NO_USER:{
		'code':ERROR_TOKEN_WRONG_NO_USER,
		'message':'token wrong, no user',
		'category':None,
	},

	ERROR_CODE_WRONG:{
		'code':ERROR_CODE_WRONG,
		'message':'code wrong',
		'category':None,
	},

	ERROR_IV_ENCRYPTED_WRONG:{
		'code':ERROR_IV_ENCRYPTED_WRONG,
		'message':'iv or encrypted_data wrong',
		'category':None,
	},

	ERROR_MONGO_GET_USER_WRONG:{
		'code':ERROR_MONGO_GET_USER_WRONG,
		'message':'get user from database wrong',
		'category':None,
	},

	ERROR_TOKEN_WRONG_ENCRYPT:{
		'code':ERROR_TOKEN_WRONG_ENCRYPT,
		'message':'token encrypt wong',
		'category':None,
	},

	ERROR_CONTENT_TYPE_NOT_JSON:{
		'code':ERROR_CONTENT_TYPE_NOT_JSON,
		'message':'content type is not json',
		'category':None,
	},


	ERROR_LOGIN_CODE_MISSING:{
		'code':ERROR_LOGIN_CODE_MISSING,
		'message':'missing code',
		'category':'login',
	},

	ERROR_LOGIN_CODE_FREQUENCY_LIMIT:{
		'code':ERROR_LOGIN_CODE_FREQUENCY_LIMIT,
		'message':'frequency limitation',
		'category':'login',
	},

	ERROR_LOGIN_CODE_WEIXIN_BUSY:{
		'code':ERROR_LOGIN_CODE_WEIXIN_BUSY,
		'message':'weixin server busy',
		'category':'login',
	},

	ERROR_LOGIN_CODE_LOST_EFFECT:{
		'code':ERROR_LOGIN_CODE_LOST_EFFECT,
		'message':'code lost effect',
		'category':'login',
	},

	ERROR_LOGIN_CODE_NO_WHY:{
		'code':ERROR_LOGIN_CODE_NO_WHY,
		'message':'failure is failure, no why',
		'category':'login',
	},

	ERROR_LOGIN_MONGO_CREATE_FAIL:{
		'code':ERROR_LOGIN_MONGO_CREATE_FAIL,
		'message':'create user failed',
		'category':'login',
	},

	ERROR_LOGIN_MONGO_UPDATE_FAIL:{
		'code':ERROR_LOGIN_MONGO_UPDATE_FAIL,
		'message':'database update failed',
		'category':'login',
	},

	ERROR_REGISTER_MISSING_IV_OR_ENCRYPTED:{
		'code':ERROR_REGISTER_MISSING_IV_OR_ENCRYPTED,
		'message':'missing iv or encrypted_data',
		'category':'register',
	},

	ERROR_REGISTER_MISSING_TOKEN:{
		'code':ERROR_REGISTER_MISSING_TOKEN,
		'message':'missing token',
		'category':'register',
	},

	ERROR_REGISTER_NO_USER:{
		'code':ERROR_REGISTER_NO_USER,
		'message':'no this user of this token',
		'category':'register',
	},


	ERROR_MISSING_WXAPP_ID:{
		'code':ERROR_MISSING_WXAPP_ID,
		'message':'missing appid',
		'category':None,
	},

	ERROR_MISSING_WXAPP_SECRET:{
		'code':ERROR_MISSING_WXAPP_SECRET,
		'message':'missing app secret',
		'category':None,
	},


	ERROR_CONFIG_WEB_NAME_WRONG:{
		'code':ERROR_CONFIG_WEB_NAME_WRONG,
		'message':'WEB_NAME wrong',
		'category':None,
	},

	ERROR_CONFIG_TOKEN_SECRET_KEY_WRONG:{
		'code':ERROR_CONFIG_TOKEN_SECRET_KEY_WRONG,
		'message':'TOKEN_SERCRET_KEY wrong',
		'category':None,
	},

	ERROR_CONFIG_TOKEN_TIMEOUT_HOURS_WRONG:{
		'code':ERROR_CONFIG_TOKEN_TIMEOUT_HOURS_WRONG,
		'message':'TOKEN_TIMEOUT_HOURS wrong',
		'category':None,
	},

	ERROR_CONFIG_TOKEN_SALT_WRONG:{
		'code':ERROR_CONFIG_TOKEN_SALT_WRONG,
		'message':'TOKEN_SALT wrong',
		'category':None,
	},

	ERROR_CONFIG_TOKEN_FIELDS_REQUIRED_WRONG:{
		'code':ERROR_CONFIG_TOKEN_FIELDS_REQUIRED_WRONG,
		'message':'TOKEN_FIELDS_REQUIRED wrong',
		'category':None,
	},

	ERROR_CONFIG_TOKEN_HEADER_FIELD_WRONG:{
		'code':ERROR_CONFIG_TOKEN_HEADER_FIELD_WRONG,
		'message':'TOKEN_HEADER_FIELD wrong',
		'category':None,
	},

	ERROR_CONFIG_LOGIN_CODE_FIELD_NAME_WRONG:{
		'code':ERROR_CONFIG_LOGIN_CODE_FIELD_NAME_WRONG,
		'message':'LOGIN_CODE_FIELD_NAME wrong',
		'category':None,
	},

	ERROR_CONFIG_UPDATE_IV_FIELD_NAME_WRONG:{
		'code':ERROR_CONFIG_UPDATE_IV_FIELD_NAME_WRONG,
		'message':'UPDATE_IV_FIELD_NAME wrong',
		'category':None,
	},

	ERROR_CONFIG_UPDATE_ENCRYPTEDDATA_FIELD_NAME_WRONG:{
		'code':ERROR_CONFIG_UPDATE_ENCRYPTEDDATA_FIELD_NAME_WRONG,
		'message':'UPDATE_ENCRYPTEDDATA_FIELD_NAME wrong',
		'category':None,
	},
}


from rest_framework.exceptions import APIException
class ApplicationException(APIException):

	def __init__(self, errcode=None, code=None):
		if errcode is None:
			detail = ('A server error occurred.')
		if code is None:
			self.code = 'error'

		if errcode is not None:
			self.detail = ERRORS[errcode]



#print ApplicationException(ERROR_CONFIG_UPDATE_ENCRYPTEDDATA_FIELD_NAME_WRONG)