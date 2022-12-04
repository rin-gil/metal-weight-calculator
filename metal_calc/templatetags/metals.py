"""Tags metals and alloys for templates"""

from django import template
from django.db.models import QuerySet

from metal_calc.models import MetalGrade, Metals


register: template.Library = template.Library()


@register.simple_tag()
def get_metal_types() -> QuerySet:
    """Returns information about metals"""
    return Metals.objects.values("id", "metal_type", "density")


@register.simple_tag()
def get_metal_alloys() -> QuerySet:
    """Returns information about metal alloys"""
    return MetalGrade.objects.values("id", "metal_type_id", "metal_grade", "density")
