"""ASGI config for metalCalculator project"""

from os import environ

from django.core.asgi import get_asgi_application
from django.core.handlers.asgi import ASGIHandler


environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application: ASGIHandler = get_asgi_application()
