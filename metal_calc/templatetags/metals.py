"""Tags metals and alloys for templates"""

from django import template
from modeltranslation.manager import MultilingualQuerySet

from metal_calc.models import MetalAlloy, Metal


register: template.Library = template.Library()


@register.simple_tag()
def get_metals() -> MultilingualQuerySet:
    """Returns information about metals"""
    return Metal.objects.values("id", "metal_name")


@register.simple_tag()
def get_metal_alloys() -> MultilingualQuerySet:
    """Returns information about metal alloys"""
    return MetalAlloy.objects.values("id", "metal_alloy", "metal_id")
