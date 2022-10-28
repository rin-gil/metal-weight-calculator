from django.contrib import admin

from .models import PageInfo, MetalShape, Metals, MetalGrade


class PageInfoAdmin(admin.ModelAdmin):
    list_display: tuple = ('title', 'description', 'keywords')
    list_display_links: tuple = ('title',)
    search_fields: tuple = ('title', 'description', 'keywords')


class MetalShapeAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'shape_name')
    list_display_links: tuple = ('shape_name',)
    search_fields: tuple = ('shape_name',)


class MetalsAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'metal_type', 'density')
    list_display_links: tuple = ('metal_type',)
    search_fields: tuple = ('metal_type',)


class MetalGradeAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'metal_type_id', 'metal_grade', 'density')
    list_display_links: tuple = ('metal_grade',)
    list_filter: tuple = ('metal_type_id',)
    search_fields: tuple = ('metal_grade',)


admin.site.register(PageInfo, PageInfoAdmin)
admin.site.register(MetalShape, MetalShapeAdmin)
admin.site.register(Metals, MetalsAdmin)
admin.site.register(MetalGrade, MetalGradeAdmin)

admin.site.site_title = 'Калькулятор веса металла'
admin.site.site_header = 'Панель администратора :: Калькулятор веса металла'
