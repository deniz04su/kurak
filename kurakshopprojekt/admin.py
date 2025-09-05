# kurakshopprojekt/admin.py
from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_original', 'phone_number')
    list_filter = ('is_original',)
    search_fields = ('name', 'phone_number')
