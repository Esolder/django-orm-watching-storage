import os
from dotenv import load_dotenv
import json

load_dotenv()
DATABASES = {'default': json.loads(os.getenv('DB_SETTINGS'))}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = False

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['localhost']


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
