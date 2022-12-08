"""metal_calc URL Configuration"""

from django.urls import path

from metal_calc.views import MetalCalcHomeView


urlpatterns: list = [path("", MetalCalcHomeView.as_view(), name="home")]
