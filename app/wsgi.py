"""WSGI config for metalCalculator project"""

from os import environ

from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application


environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application: WSGIHandler = get_wsgi_application()
