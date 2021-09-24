from django.contrib import admin
from .models import Product
from .models import UserProfile,User


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile)
