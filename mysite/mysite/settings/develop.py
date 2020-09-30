from .base import * # NOQA
DEBUG=True
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'USER':'root',
        'NAME':'mysite',
    }
}