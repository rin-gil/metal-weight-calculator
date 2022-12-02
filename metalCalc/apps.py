"""Configuration of the metalCalc application"""

from django.apps import AppConfig


class MetalCalcConfig(AppConfig):
    """Configuration of the metalCalc application"""
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "metalCalc"
    verbose_name: str = "Калькулятор веса металла"
