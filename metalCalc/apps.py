from django.apps import AppConfig


class MetalCalcConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'metalCalc'
    verbose_name: str = 'Калькулятор веса металла'
