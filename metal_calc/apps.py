"""Configuration of the metal_calc application"""

from django.apps import AppConfig


class MetalCalcConfig(AppConfig):
    """Configuration of the metal_calc application"""

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "metal_calc"
    verbose_name: str = "Калькулятор веса металла"
