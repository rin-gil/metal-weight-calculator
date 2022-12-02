"""Models for the admin panel"""

from django.contrib import admin

from metalCalc.models import MetalGrade, Metals, MetalShape, PageInfo


class PageInfoAdmin(admin.ModelAdmin):
    """Displaying the PageInfoAdmin model in the admin panel"""
    list_display: tuple = ("title", "description", "keywords")
    list_display_links: tuple = ("title",)
    search_fields: tuple = ("title", "description", "keywords")


class MetalShapeAdmin(admin.ModelAdmin):
    """Displaying MetalShapeAdmin XXX model in the admin panel"""
    list_display: tuple = ("id", "shape_name")
    list_display_links: tuple = ("shape_name",)
    search_fields: tuple = ("shape_name",)


class MetalsAdmin(admin.ModelAdmin):
    """Displaying the MetalsAdmin model in the admin panel"""
    list_display: tuple = ("id", "metal_type", "density")
    list_display_links: tuple = ("metal_type",)
    search_fields: tuple = ("metal_type",)


class MetalGradeAdmin(admin.ModelAdmin):
    """Displaying the MetalGradeAdmin model in the admin panel"""
    list_display: tuple = ("id", "metal_type_id", "metal_grade", "density")
    list_display_links: tuple = ("metal_grade",)
    list_filter: tuple = ("metal_type_id",)
    search_fields: tuple = ("metal_grade",)


admin.site.register(PageInfo, PageInfoAdmin)
admin.site.register(MetalShape, MetalShapeAdmin)
admin.site.register(Metals, MetalsAdmin)
admin.site.register(MetalGrade, MetalGradeAdmin)

admin.site.site_title = "Калькулятор веса металла"
admin.site.site_header = "Панель администратора :: Калькулятор веса металла"
