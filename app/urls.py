"""metalCalculator URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from app.settings import DEBUG

from metal_calc.views import page_not_found


urlpatterns: list = [
    path("", include("metal_calc.urls")),
]

if DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]

handler404 = page_not_found
