import os
import socket
from datetime import timedelta

# import cloudinary
from corsheaders.defaults import default_headers
from django.conf import settings

REST_FRAMEWORK_FORMAT_FIELD_NAMES = 'capitalize'
REST_FRAMEWORK_PLURALIZE_TYPES = True
REST_USE_JWT = True
# ACCOUNT_ADAPTER = 'common.accountadapter.CustomAccountAdapter'
# ACCOUNT_ADAPTER = 'Authentication.Rest.views.CustomAccountAdapter'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'NON_FIELD_ERRORS_KEY': 'global',
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(days=30),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',

    # 'JWT_ENCODE_HANDLER':
    # 'rest_framework_jwt.utils.jwt_encode_handler',
    # 'JWT_DECODE_HANDLER':
    # 'rest_framework_jwt.utils.jwt_decode_handler',
    # 'JWT_PAYLOAD_HANDLER':
    # 'rest_framework_jwt.utils.jwt_payload_handler',
    # 'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    # 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    # 'JWT_RESPONSE_PAYLOAD_HANDLER':
    # 'rest_framework_jwt.utils.jwt_response_payload_handler',

    # 'JWT_SECRET_KEY': 'SECRET_KEY',
    # 'JWT_GET_USER_SECRET_KEY': None,
    # 'JWT_PUBLIC_KEY': None,
    # 'JWT_PRIVATE_KEY': None,
    # 'JWT_ALGORITHM': 'HS256',
    # 'JWT_VERIFY': True,
    # 'JWT_VERIFY_EXPIRATION': True,
    # 'JWT_LEEWAY': 0,
    # 'JWT_EXPIRATION_DELTA': timedelta(days=30),
    # 'JWT_AUDIENCE': None,
    # 'JWT_ISSUER': None,
    # 'JWT_ALLOW_REFRESH': False,
    # 'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=30),
    # 'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    # 'JWT_AUTH_COOKIE': None,

}
'''CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    CUSTOM_FRONTEND_SITE_URL,
    'http://127.0.0.1:8000'
    #
)'''




CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

'''CORS_ALLOW_HEADERS = default_headers + (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'access-control-allow-headers',
    'Access-Control-Allow-Origin',
)'''
