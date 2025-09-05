from django.contrib import admin
from .models import Category, MenuItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('priority','title','parent','image')


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title','priority','category','get_parent','price','is_available','image')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'description')
    def get_parent(self, obj):
        return obj.category.parent
    get_parent.short_description = 'Parent Category'

admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
