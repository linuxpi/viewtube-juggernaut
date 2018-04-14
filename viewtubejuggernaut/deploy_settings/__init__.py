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
