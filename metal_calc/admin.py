"""Models for the admin panel"""

from django.contrib import admin

from metal_calc.models import MetalAlloy, Metal, MetalShape, PageInfo


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

    list_display: tuple = ("id", "metal_name", "density")
    list_display_links: tuple = ("metal_name",)
    search_fields: tuple = ("metal_name",)


class MetalGradeAdmin(admin.ModelAdmin):
    """Displaying the MetalGradeAdmin model in the admin panel"""

    list_display: tuple = ("id", "metal", "metal_alloy", "density")
    list_display_links: tuple = ("metal_alloy",)
    list_filter: tuple = ("metal",)
    search_fields: tuple = ("metal_alloy",)


admin.site.register(PageInfo, PageInfoAdmin)
admin.site.register(MetalShape, MetalShapeAdmin)
admin.site.register(Metal, MetalsAdmin)
admin.site.register(MetalAlloy, MetalGradeAdmin)

admin.site.site_title = "Калькулятор веса металла"
admin.site.site_header = "Панель администратора :: Калькулятор веса металла"
