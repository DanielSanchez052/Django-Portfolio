"""
WSGI config for Portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

debug = config('DEBUG', default=False, cast=bool)
settings_module = 'Portfolio.settings.production' if not debug else 'Portfolio.settings.local'


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      settings_module)

application = get_wsgi_application()
