"""metalCalculator URL Configuration"""

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from app.settings import DEBUG

from metal_calc.views import custom404


urlpatterns: list = i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("metal_calc.urls")),
)

if DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]

handler404 = custom404
