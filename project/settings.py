import os

from dotenv import load_dotenv
from environs import Env

load_dotenv()

env = Env()
env.read_env()

db_engine = os.getenv('ENGINE')
db_host = os.getenv('HOST')
port = os.getenv('PORT')
user_name = os.getenv('NAME')
user_type = os.getenv('USER')
user_password = os.getenv('PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'HOST': db_host,
        'PORT': port,
        'NAME': user_name,
        'USER': user_type,
        'PASSWORD': user_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
