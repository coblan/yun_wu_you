from .base import *

DATABASES = {
    'default': {
        'NAME': 'yun_wu_you',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root123456789',
        'HOST': '127.0.0.1', 
        'PORT': '3306',        
      },
    }

ALLOWED_HOSTS = ['yzdd360.com', 'yun.enjoyst.com','www.yzdd360.com']