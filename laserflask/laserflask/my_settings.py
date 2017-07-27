from .settings import *

TIME_ZONE = 'Europe/Kiev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
    }
}

LANGUAGE_CODE = 'uk-ua'

ITEMS_ON_PAGE = 3

AUTH_USER_MODEL = 'accounts.User'
