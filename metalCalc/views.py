from django.shortcuts import render
from django.views.generic import TemplateView

from metalCalc.services import PAGE_INFO, SITE_URL, METAL_SHAPES, METAL_TYPES, METAL_ALLOYS, \
    _get_context_data_for_calculator_fields


class MetalCalcHomeView(TemplateView):
    """
    Model representing a type of metal shape.

    Attributes
        template_name : str
            page template path

        context : dict
            dictionary of data used to display the template

            page_info : QuerySet
                information about the page - title, description, keywords
            site_url : str
                site domain - from settings.ALLOWED_HOSTS
            shapes : QuerySet
                names of cross-sectional profiles
            metal_types : QuerySet
                different types of metals and their densities
            metal_alloys : QuerySet
                types of metal alloys and their density
            shape_selected : int
                cross-sectional profile selected by default
            metal_type_selected : int
                default metal type selected
            metal_alloy_selected : int
                metallic alloy selected by default
            error_message : bool
                any errors in the input data
    """
    template_name: str = 'metalCalc/index.html'
    context: dict = {
        'page_info': PAGE_INFO,
        'site_url': SITE_URL,
        'shapes': METAL_SHAPES,
        'metal_types': METAL_TYPES,
        'metal_alloys': METAL_ALLOYS,
        'shape_selected': 1,
        'metal_type_selected': 1,
        'metal_alloy_selected': 0,
        'error_message': False
    }

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name, context=self.context.copy())

    def post(self, request, *args, **kwargs):
        context = _get_context_data_for_calculator_fields(request=request.POST, context=self.context.copy())
        return render(request=request, template_name=self.template_name, context=context)


def page_not_found(request, exception):
    """
    Displays a 404 application error page.

    :param request: request
    :param exception: exception
    :return: render
    """
    return render(request=request, template_name='metalCalc/404.html', status=404)
