"""Tags site information for templates"""

from django import template

from app.settings import ALLOWED_HOSTS
from metal_calc.models import PageInfo


register: template.Library = template.Library()


@register.simple_tag()
def get_site_info() -> dict:
    """Returns information about the site"""
    site_info: PageInfo = PageInfo.objects.get(pk=1)
    return {
        "title": site_info.title,
        "description": site_info.description,
        "keywords": site_info.keywords,
        "site_url": ALLOWED_HOSTS[0],
    }
