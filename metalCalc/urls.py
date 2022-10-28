from django.urls import path
from django.views.decorators.cache import cache_page

from .views import MetalCalcHomeView

urlpatterns: list = [
    path('', cache_page(0)(MetalCalcHomeView.as_view()), name='home'),
]
