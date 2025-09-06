from django.contrib import admin
from .models import User, Profile, Category, Product, ProductMedia, ProductComment, ProductReaction, ProductStatus, ChatMessage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'created_at')

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(ProductMedia)
admin.site.register(ProductComment)
admin.site.register(ProductReaction)
admin.site.register(ProductStatus)
admin.site.register(ChatMessage)
