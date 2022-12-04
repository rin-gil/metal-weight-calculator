"""metal_calc views Configuration"""

from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import Resolver404
from django.views.generic import TemplateView

from metal_calc.services import ContextData, default_context_data, get_context_data_for_calculator_fields


class MetalCalcHomeView(TemplateView):
    """Displaying information on the pages of the site"""
    template_name: str = "metalCalc/index.html"
    context: ContextData = default_context_data

    def get(self, request: WSGIRequest, **kwargs: Any) -> HttpResponse:
        """Displaying a page during a GET request"""
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request: WSGIRequest) -> HttpResponse:
        """Displaying a page during a POST request"""
        context = get_context_data_for_calculator_fields(request=request.POST, context=self.context.copy())
        return render(request=request, template_name=self.template_name, context=context)


def page_not_found(request: WSGIRequest, exception: Resolver404) -> HttpResponse:
    """Displays a 404 application error page"""
    context: dict = {"wrong_url": f"{exception.args[0]['path']}"}
    return render(request=request, template_name="metalCalc/404.html", context=context, status=404)
