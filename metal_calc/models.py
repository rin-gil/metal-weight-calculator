"""The module describes the models used in the metal_calc application"""

from django.db import models


class PageInfo(models.Model):
    """The model defines the title, description, keywords and meta tags for website pages"""
    title: str = models.CharField(unique=True, max_length=60, verbose_name="Название страницы")
    description: str = models.CharField(max_length=150, verbose_name="Описание страницы")
    keywords: str = models.CharField(max_length=250, verbose_name="Ключевые слова")

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        """Defines the representation of the model in the program"""
        verbose_name: str = "Страница сайта"
        verbose_name_plural: str = "Страницы сайта"
        ordering: tuple = ("title",)


class MetalShape(models.Model):
    """Model representing a type of metal shape"""
    shape_name: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name="Название профиля")

    def __str__(self) -> str:
        return str(self.shape_name)

    class Meta:
        """Defines the representation of the model in the program"""
        verbose_name: str = "Профиль металлопроката"
        verbose_name_plural: str = "Профили металлопроката"
        ordering: tuple = ("shape_name",)


class Metal(models.Model):
    """The model describes different kinds of metals"""
    metal_name: str = models.CharField(unique=True, max_length=10, db_index=True, verbose_name="Название металла")
    density: int = models.SmallIntegerField(verbose_name="Плотность металла, кг/м³")

    def __str__(self) -> str:
        return str(self.metal_name)

    class Meta:
        """Defines the representation of the model in the program"""
        verbose_name: str = "Металл"
        verbose_name_plural: str = "Металлы"
        ordering: tuple = ("metal_name",)


class MetalAlloy(models.Model):
    """The model describes different grades of metal alloys"""
    metal: int = models.ForeignKey(to=Metal, on_delete=models.CASCADE, verbose_name="Металл")
    metal_alloy: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name="Название сплава")
    density: int = models.SmallIntegerField(verbose_name="Плотность сплава, кг/м³")

    def __str__(self) -> str:
        return str(self.metal_alloy)

    class Meta:
        """Defines the representation of the model in the program"""
        verbose_name: str = "Сплав"
        verbose_name_plural: str = "Сплавы"
        ordering: tuple = ("metal", "metal_alloy")
