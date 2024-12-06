from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Product


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'parentId', 'level',
    list_display_links = 'id', 'name'
    ordering = ('id',)


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = 'id', 'name', 'price', 'category_list', 'inStock', 'image'
    list_display_links = 'id', 'name'
    ordering = ('id',)
    search_fields = ('name',)
    list_filter = ('category', 'inStock', 'price',)

    @staticmethod
    def category_list(obj):
        return ', '.join([c.name for c in obj.category.all()])

