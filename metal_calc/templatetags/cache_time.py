"""Tag cache_timeout for templates"""

from django import template

from app.settings import CACHE_TIMEOUT


register: template.Library = template.Library()


@register.simple_tag()
def get_cache_timeout() -> int:
    """Returns the value of cache storage time"""
    return CACHE_TIMEOUT
