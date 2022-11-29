from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = [config('WEBSITE_HOSTNAME')
                 ] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://' + config('WEBSITE_HOSTNAME')
                        ] if 'WEBSITE_HOSTNAME' in os.environ else []

hostname = config('DBHOST')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DBNAME'),
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': config('DBUSER'),
        'PASSWORD': config('DBPASS')
    }
}
