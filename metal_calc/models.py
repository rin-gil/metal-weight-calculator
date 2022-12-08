"""The module describes the models used in the metal_calc application"""

from typing import Any

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.settings import LANGUAGES


class PageInfo(models.Model):
    """The model defines the title, description, keywords and meta tags for website pages"""

    title: str = models.CharField(unique=True, max_length=60, verbose_name=_("Page title"))
    description: str = models.CharField(max_length=150, verbose_name=_("Page description"))
    keywords: str = models.CharField(max_length=250, verbose_name=_("Keywords"))

    def __str__(self) -> str:
        return self.title

    def save(self, *args: Any, **kwargs: Any) -> None:
        for _ in LANGUAGES:
            key: str = make_template_fragment_key(fragment_name="site_info", vary_on=[_[0]])
            cache.delete(key)
        for _ in LANGUAGES:
            key = make_template_fragment_key(fragment_name="site_title", vary_on=[_[0]])
            cache.delete(key)
        super().save(*args, **kwargs)

    class Meta:
        """Defines the representation of the model in the program"""

        verbose_name: str = _("Site page")
        verbose_name_plural: str = _("Site pages")
        ordering: tuple = ("title",)


class MetalShape(models.Model):
    """Model representing a type of metal shape"""

    shape_name: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name=_("Profile name"))

    def __str__(self) -> str:
        return self.shape_name

    def save(self, *args: Any, **kwargs: Any) -> None:
        for _ in LANGUAGES:
            key: str = make_template_fragment_key(fragment_name="header", vary_on=[_[0]])
            cache.delete(key)
        super().save(*args, **kwargs)

    class Meta:
        """Defines the representation of the model in the program"""

        verbose_name: str = _("Rolled metal profile")
        verbose_name_plural: str = _("Rolled metal profiles")
        ordering: tuple = ("shape_name",)


class Metal(models.Model):
    """The model describes different kinds of metals"""

    metal_name: str = models.CharField(unique=True, max_length=10, db_index=True, verbose_name=_("Metal name"))
    density: int = models.SmallIntegerField(verbose_name=_("Metal density, kg/m³"))

    def __str__(self) -> str:
        return self.metal_name

    def save(self, *args: Any, **kwargs: Any) -> None:
        for _ in LANGUAGES:
            key: str = make_template_fragment_key(fragment_name="form_select_metals", vary_on=[_[0]])
            cache.delete(key)
        super().save(*args, **kwargs)

    class Meta:
        """Defines the representation of the model in the program"""

        verbose_name: str = _("Metal")
        verbose_name_plural: str = _("Metals")
        ordering: tuple = ("metal_name",)


class MetalAlloy(models.Model):
    """The model describes different grades of metal alloys"""

    metal: int = models.ForeignKey(to=Metal, on_delete=models.CASCADE, verbose_name=_("Metal"))
    metal_alloy: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name=_("Name of alloy"))
    density: int = models.SmallIntegerField(verbose_name=_("Alloy density, kg/m³"))

    def __str__(self) -> str:
        return self.metal_alloy

    def save(self, *args: Any, **kwargs: Any) -> None:
        for _ in LANGUAGES:
            key: str = make_template_fragment_key(fragment_name="form_select_metals", vary_on=[_[0]])
            cache.delete(key)
        super().save(*args, **kwargs)

    class Meta:
        """Defines the representation of the model in the program"""

        verbose_name: str = _("Alloy")
        verbose_name_plural: str = _("Alloys")
        ordering: tuple = ("metal", "metal_alloy")
