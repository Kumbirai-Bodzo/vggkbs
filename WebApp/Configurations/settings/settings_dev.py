from django.core.files.storage import FileSystemStorage

from .base_settings import *

# DEBUG = int(os.environ.get('DEBUG', default=1))
DEBUG = True
CUSTOM_DOMAIN_NAME = 'Configurations'
ALLOWED_HOSTS = ['*', '127.0.0.1']

# Host Backend urls
CUSTOM_BACKEND_SITE_URL = 'http://localhost:8000'
CUSTOM_IMAGES_HOST_URL = CUSTOM_BACKEND_SITE_URL #CUSTOM_BACKEND_SITE_URL

# Host Frontend urls
CUSTOM_FRONTEND_SITE_URL = 'http://localhost:4200'
CUSTOM_PASSWORD_RESET_PAGE_URL = CUSTOM_FRONTEND_SITE_URL + '/auth/set/password-confirm-reset/confirm'

CUSTOM_ACCOUNT_CONFIRM_EMAIL_URL = CUSTOM_FRONTEND_SITE_URL + "/auth/set/account-confirm-email/?key={0}"
FILE_STORAGE = FileSystemStorage(location=settings.MEDIA_ROOT)
DEFAULT_FILE_STORAGE = FileSystemStorage(location=settings.MEDIA_ROOT)
# GOOGLE_API_KEY = 'AIzaSyBA3YuUG_aXCK26oQJZ4nm6LZzEZmomBSw'
# PLACES_MAPS_API_KEY='AIzaSyBA3YuUG_aXCK26oQJZ4nm6LZzEZmomBSw'
# PLACES_MAP_WIDGET_HEIGHT=480
# PLACES_MAP_OPTIONS='{"center": { "lat": 38.971584, "lng": -95.235072 }, "zoom": 10}'
# PLACES_MARKER_OPTIONS='{"draggable": true}'

# CLOUDNARY CONFIGURATIONS
#DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
# 

#DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'adventurebookings',
#     'API_KEY': '758798491894838',
#     'API_SECRET': 'RErU6IiZJamQPCUfOwndWRiLRho',
#     }

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'elitecode',
#     'API_KEY': '488823284154167',
#     'API_SECRET': 'SGVVIikZyAXkFO5jZXHYyvdOryI',
# }

# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR+'/backups'}
# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
# DBBACKUP_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
# DBBACKUP_STORAGE_OPTIONS = {
#     'oauth2_access_token': '6KRDYYGHKXcAAAAAAAAAASLadZj5k7kdcTimHgdnnp1JoEaM0rT_eCqaosMFzfiE',
# }
# DBBACKUP_FILENAME_TEMPLATE = '{datetime}-{databasename}.{extension}'

# CREDENTIAL_FOLDER = os.path.join(BASE_DIR, 'credentials')
# # print(CREDENTIAL_FOLDER)
# CREDENTIAL_FILES = {
#     'drive': 'adventure-bookings-303814-5f3dbed6ff55.json',
# }
# BACKUP_LOCAL_DB_DIR = os.path.join(BASE_DIR)
# BACKUP_GDRIVE_DIR = 'django_backup'
# BACKUP_GDRIVE_DB = BACKUP_GDRIVE_DIR + '/db'

# adventure-bookings-303814-5f3dbed6ff55.json
# AWS CONFIGURATIONS
# AWS_USERNAME = 'zim-bookings-user'
# AWS_GROUP = 'zim-bookings-group'
# AWS_ACCESS_KEY_ID = 'AKIAZVZ7LYAZ4ENZN74I'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'sibtc-static'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'
#zim-bookings-bucket-policy
#zim-bookings-bucket


