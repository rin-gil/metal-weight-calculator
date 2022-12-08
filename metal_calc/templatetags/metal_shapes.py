"""Rolled metal shapes tags for templates"""

from django import template
from modeltranslation.manager import MultilingualQuerySet

from metal_calc.models import MetalShape


register: template.Library = template.Library()


@register.simple_tag()
def get_metal_shapes() -> MultilingualQuerySet:
    """Returns information about rolled steel shapes"""
    return MetalShape.objects.values("id", "shape_name")
