"""Registering Models for Translation"""

from modeltranslation.translator import translator, TranslationOptions

from metal_calc.models import MetalAlloy, Metal, MetalShape, PageInfo


class PageInfoTranslationOptions(TranslationOptions):
    """Defining fields for translation in the PageInfo model"""

    fields: tuple = ("title", "description", "keywords")


class MetalShapeTranslationOptions(TranslationOptions):
    """Defining fields for translation in the MetalShape model"""

    fields: tuple = ("shape_name",)


class MetalTranslationOptions(TranslationOptions):
    """Defining fields for translation in the Metal model"""

    fields: tuple = ("metal_name",)


class MetalAlloyTranslationOptions(TranslationOptions):
    """Defining fields for translation in the MetalAlloy model"""

    fields: tuple = ("metal_alloy",)


translator.register(PageInfo, PageInfoTranslationOptions)
translator.register(MetalShape, MetalShapeTranslationOptions)
translator.register(Metal, MetalTranslationOptions)
translator.register(MetalAlloy, MetalAlloyTranslationOptions)
