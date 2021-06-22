
from django.core.files.storage import FileSystemStorage

from .base_settings import *

PROD_APPS =[
 # 'gdstorage'
]

INSTALLED_APPS += PROD_APPS

try:
    # pyright: reportMissingImports=false
    import dj_database_url

    # FILE_STORAGE = FileSystemStorage(location=settings.MEDIA_ROOT)
    # DEFAULT_FILE_STORAGE = FileSystemStorage(location=settings.MEDIA_ROOT)
    
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'elitecode',
        'API_KEY': '488823284154167',
        'API_SECRET': 'SGVVIikZyAXkFO5jZXHYyvdOryI',
        }


    import cloudinary
    import cloudinary.api
    import cloudinary.uploader

    cloudinary.config( 
    cloud_name ='elitecode',
    api_key = '488823284154167',
    api_secret = 'SGVVIikZyAXkFO5jZXHYyvdOryI',

    )

    # define postgrel database connections

    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)
    DATABASES['default']['CONN_MAX_AGE'] = 500
    print('<------------ USING PRODUCTION SETTINGS ------------>')
    
except Exception:
    print('refused production environment')
    pass
    # logging.error('<------------ THIS ENVIRONMENT IS NOT AVAILABLE ------------>')

CUSTOM_DOMAIN_NAME = 'https://adventurebookings.net' # 'https://docking-vggkbs.herokuapp.com'
# SECRET_KEY = '5%5e%41(8ps!r36)r=i(ismmdcf0%@*zmchhg*4-5_i-0cbryf'

ALLOWED_HOSTS = ['*', CUSTOM_DOMAIN_NAME]

# Host Backend urls
CUSTOM_BACKEND_SITE_URL = CUSTOM_DOMAIN_NAME
CUSTOM_IMAGES_HOST_URL = '' # CUSTOM_BACKEND_SITE_URL
# Host Frontend urls
CUSTOM_FRONTEND_SITE_URL = CUSTOM_DOMAIN_NAME
# Links
CUSTOM_PASSWORD_RESET_PAGE_URL = CUSTOM_FRONTEND_SITE_URL + '/auth/account/password-confirm-reset/confirm'
CUSTOM_ACCOUNT_CONFIRM_EMAIL_URL = CUSTOM_FRONTEND_SITE_URL + "/auth/account-confirm-email/?key={0}"
DEBUG = True

