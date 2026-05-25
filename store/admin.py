from django.contrib import admin
from .models import Tshirt
from .models import Jeans


@admin.register(Tshirt)
class TshirtAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'brand',
        'color',
        'size',
        'price',
        'stock',
    )

    search_fields = ('name', 'brand')
    list_filter = ('brand', 'color', 'size')

@admin.register(Jeans)
class JeansAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'brand',
        'fit',
        'size',
        'price',
        'stock',
    )

    search_fields = ('name', 'brand')
    list_filter = ('fit', 'size', 'brand')