from django.contrib import admin
from .models import Product, Category, Manufacturer



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'stock_no',
        'name',
        'category',
        'suits',
        'price',
        'rating',
        'image',
    )

    ordering = ('stock_no',)
    
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',        
    )

    ordering = ('friendly_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',        
    )

    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Category, CategoryAdmin)
