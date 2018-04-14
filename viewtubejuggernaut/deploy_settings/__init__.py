from viewtubejuggernaut.settings import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.pythonanywhere.com'
]

SECRET_KEY = get_from_env("SECRET_KEY")