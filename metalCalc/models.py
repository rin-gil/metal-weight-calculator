"""
The module describes the models used in the application.

Classes
    PageInfo :
        The model represents the title, description, keywords and other meta tags for each page of the site.
    MetalShape :
        A model representing a type of metal shape.
    Metals :
        The model describes different kinds of metals.
    MetalGrade :
        The model describes different grades of metal alloys.
"""

from django.db import models


class PageInfo(models.Model):
    """
    The model represents the title, description, keywords and other meta tags for each page of the site.

    Attributes
        id: int
            page identifier
        title : str
            page title
        description : str
            page description
        keywords: str
            keywords
    """
    title: str = models.CharField(unique=True, max_length=60, verbose_name='Название страницы')
    description: str = models.CharField(max_length=150, verbose_name='Описание страницы')
    keywords: str = models.CharField(max_length=250, verbose_name='Ключевые слова')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: str = 'Информация о страницы'
        verbose_name_plural: str = 'Информация о страницах'
        ordering: tuple = ('title',)


class MetalShape(models.Model):
    """
    Model representing a type of metal shape.

    Attributes
        id : int
            shape identifier
        shape_name : str
            name of the metal shape
    """
    shape_name: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.shape_name

    class Meta:
        verbose_name: str = 'Профиль металла'
        verbose_name_plural: str = 'Профили металла'
        ordering: tuple = ('shape_name',)


class Metals(models.Model):
    """
    The model describes different kinds of metals.

    Attributes
        id : int
            metal identifier
        metal_type : str
            metal name
        density : int
            metal alloy density
    """
    metal_type: str = models.CharField(unique=True, max_length=10, db_index=True, verbose_name='Металл')
    density: int = models.SmallIntegerField(verbose_name='Плотность материала, кг/м3')

    def __str__(self):
        return self.metal_type

    class Meta:
        verbose_name: str = 'Металл'
        verbose_name_plural: str = 'Металлы'
        ordering: tuple = ('metal_type',)


class MetalGrade(models.Model):
    """
    The model describes different grades of metal alloys.

    Attributes
        metal_type_id : int
            metal type identifier
        metal_grade : str
            grade name
        density : int
            metal alloy density
    """
    metal_type_id: int = models.ForeignKey(to=Metals, on_delete=models.CASCADE, verbose_name='Металл')
    metal_grade: str = models.CharField(unique=True, max_length=20, db_index=True, verbose_name='Марка металла')
    density: int = models.SmallIntegerField(verbose_name='Плотность сплава, кг/м3')

    def __str__(self):
        return self.metal_grade

    class Meta:
        verbose_name: str = 'Марка металла'
        verbose_name_plural: str = 'Марки металлов'
        ordering: tuple = ('metal_type_id', 'metal_grade')
