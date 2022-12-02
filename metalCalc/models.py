"""The module describes the models used in the metalCalc application"""

from django.db import models


class PageInfo(models.Model):
    """The model defines the title, description, keywords and meta tags for website pages"""
    title: str = models.CharField(unique=True, max_length=60, verbose_name="Название")
    description: str = models.CharField(max_length=150, verbose_name="Описание")
    keywords: str = models.CharField(max_length=250, verbose_name="Ключевые слова")

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        """Defines the representation of the model in the program"""
        verbose_name: str = "Страница"
        verbose_name_plural: str = "Страницы"
        ordering: tuple = ("title",)


class MetalShape(models.Model):
    """Model representing a type of metal shape"""
    shape_name: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name="Название")

    def __str__(self) -> str:
        return str(self.shape_name)

    class Meta:
        """Defines the representation of the model in the program"""
        verbose_name: str = "Профиль металла"
        verbose_name_plural: str = "Профили металла"
        ordering: tuple = ("shape_name",)


class Metals(models.Model):
    """The model describes different kinds of metals"""
    metal_type: str = models.CharField(unique=True, max_length=10, db_index=True, verbose_name="Металл")
    density: int = models.SmallIntegerField(verbose_name="Плотность материала, кг/м³")

    def __str__(self) -> str:
        return str(self.metal_type)

    class Meta:
        """Defines the representation of the model in the program"""
        verbose_name: str = "Металл"
        verbose_name_plural: str = "Металлы"
        ordering: tuple = ("metal_type",)


class MetalGrade(models.Model):
    """The model describes different grades of metal alloys"""
    metal_type_id: int = models.ForeignKey(to=Metals, on_delete=models.CASCADE, verbose_name="Металл")
    metal_grade: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name="Марка металла")
    density: int = models.SmallIntegerField(verbose_name="Плотность сплава, кг/м³")

    def __str__(self) -> str:
        return str(self.metal_grade)

    class Meta:
        """Defines the representation of the model in the program"""
        verbose_name: str = "Марка металла"
        verbose_name_plural: str = "Марки металлов"
        ordering: tuple = ("metal_type_id", "metal_grade")
