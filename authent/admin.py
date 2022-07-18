from django.contrib import admin
from .models import Category, Product, Cart, SubCategory
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
# admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Cart)
