from viewtubejuggernaut.settings import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.pythonanywhere.com'
]

SECRET_KEY = get_from_env('SECRET_KEY')

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': get_from_env('DB_NAME'),
    'USER': get_from_env('DB_USER'),
    'PASSWORD': get_from_env('DB_PASSWORD'),
    'HOST': get_from_env('DB_HOST'),
}

#set S3 as the place to store your files.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = get_from_env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_from_env('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = get_from_env('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'

#static media settings
STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'

MEDIA_URL = STATIC_URL + 'media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'))

STATIC_ROOT = 'staticfiles'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
