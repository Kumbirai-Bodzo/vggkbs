EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Google Emails Server
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'zipthecode@gmail.com'
# EMAIL_HOST_PASSWORD = 'zipthename@263'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
CUSTOM_FROM_RESERVATIONS_EMAIL = 'reservations@adventurebookings.net'
CUSTOM_FROM_SUPPORT_EMAIL = 'support@adventurebookings.net'
#CUSTOM_DEFAULT_DEV_EMAIL = 'support@adventurebookings.net'
#DEFAULT_FROM_EMAIL= 'support@adventurebookings.net'
# Email Backends
DEFAULT_FROM_EMAIL =  'reservations@adventurebookings.net'
# Private Email server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'mail.privateemail.com'
EMAIL_HOST_USER = 'reservations@adventurebookings.net'
EMAIL_HOST_PASSWORD = 'namecheap263@0771146083'
EMAIL_PORT = 465




# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = "email"

ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = '(adventurebookings.net) '

SOCIALACCOUNT_ADAPTER = 'Authentication.Social.views.CustomSocialAccountAdapter'
#SOCIALACCOUNT_ADAPTER = 'Authentication.Social.views.CustomSocialAccountAdapter'
# ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'  //causes rest and social not use username

REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'Authentication.Rest.serializers.all_serializer.RegisterSerializer',
      # 'LOGIN_SERIALIZER': 'Authentication.Rest.serializers.all_serializer.LoginUserSerializer',
}


#ACCOUNT_ADAPTER = 'Authentication.Rest.views.CustomAccountAdapter'

# 'zipthecode@gmail.com'
# 'zipthename@263'

# sendgrid Emails Server
'''EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'bodzok@gmail.com'
EMAIL_HOST_PASSWORD = 'G@0771146083'
EMAIL_PORT = 465
EMAIL_USE_TLS = True'''
#SITE_ID = 1
# ACCOUNT_EMAIL_VERIFICATION = True
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True   
# ACCOUNT_USERNAME_REQUIRED = True
# # ACCOUNT_USERNAME_REQUIRED = False
# REGISTER_VERIFICATION_ENABLED = True
# # REGISTER_VERIFICATION_AUTO_LOGIN = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


# User account preferences

# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'http://localhost/4200/'
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'http://localhost/4200/'
ADMINS = (
    ('Kumbirai', 'bodzok@gmail.com'),
)
MANAGERS = ADMINS

# ALLOWED_HOSTS = []
#ACCOUNT_USER_MODEL_USERNAME_FIELD = None


# v = Authentication.views import CustomAccountAdapter
# An email verification URL that the client will pick up.

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        # AdventureBookingsProject
        'APP': {
            'client_id': '308204037181-5n2impuufdg4aai5m7viub9adnd3lbes.apps.googleusercontent.com',
            'secret': 'aL4jdtnT9-vJGGMW3PX5hmx0',
            'key': ''
        }
    },
    'facebook': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '799295550873748',
            'secret': '12a44bb7f721552a5c6f37cad87cb3a0',
            'key': ''
        }
    }
}

# Rest Framework Preferences


# sigup email verification
# ACCOUNT_ADAPTER = 'common.accountadapter.CustomAccountAdapter'


'''REST_REGISTRATION2 = {

    'REGISTER_VERIFICATION_EMAIL_TEMPLATES': {
        'subject': 'rest_registration/register/subject.txt',
        'html_body': 'rest_registration/register/body.html',
    },
}'''

'''SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],

        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}'''


# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'
