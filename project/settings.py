import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DJ_DB_ENGINE"),
        'HOST': os.getenv("DJ_DB_HOST"),
        'PORT': os.getenv("DJ_DB_PORT"),
        'NAME': os.getenv("DJ_DB_NAME"),
        'USER': os.getenv("DJ_DB_USER"),
        'PASSWORD': os.getenv("DJ_DB_PASSWORD")
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = os.getenv('DEBUG', False)

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
