"""metalCalculator URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from app.settings import DEBUG

from metalCalc.views import page_not_found


urlpatterns: list = [
    path("", include("metalCalc.urls")),
]

if DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]

handler404 = page_not_found
