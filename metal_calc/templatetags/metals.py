"""Tags metals and alloys for templates"""

from django import template
from django.db.models import QuerySet

from metal_calc.models import MetalAlloy, Metal


register: template.Library = template.Library()


@register.simple_tag()
def get_metals() -> QuerySet:
    """Returns information about metals"""
    return Metal.objects.values("id", "metal_name", "density")


@register.simple_tag()
def get_alloys() -> QuerySet:
    """Returns information about metal alloys"""
    return MetalAlloy.objects.values("id", "metal_alloy", "density", "metal_id")
