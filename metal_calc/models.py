"""The module describes the models used in the metal_calc application"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class PageInfo(models.Model):
    """The model defines the title, description, keywords and meta tags for website pages"""

    title: str = models.CharField(unique=True, max_length=60, verbose_name=_("Page title"))
    description: str = models.CharField(max_length=150, verbose_name=_("Page description"))
    keywords: str = models.CharField(max_length=250, verbose_name=_("Keywords"))

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        """Defines the representation of the model in the program"""

        verbose_name: str = _("Site page")
        verbose_name_plural: str = _("Site pages")
        ordering: tuple = ("title",)


class MetalShape(models.Model):
    """Model representing a type of metal shape"""

    shape_name: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name=_("Profile name"))

    def __str__(self) -> str:
        return str(self.shape_name)

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
        return str(self.metal_name)

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
        return str(self.metal_alloy)

    class Meta:
        """Defines the representation of the model in the program"""

        verbose_name: str = _("Alloy")
        verbose_name_plural: str = _("Alloys")
        ordering: tuple = ("metal", "metal_alloy")
