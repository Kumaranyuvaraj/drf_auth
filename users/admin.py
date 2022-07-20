from django.contrib import admin
from users.models import Category, Product, Cart, SubCategory,User

from django.contrib.auth.admin import UserAdmin


# Register your models here.

class UserAdmin(UserAdmin):

    model = User()
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Category)
admin.site.register(SubCategory)
# admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(User,UserAdmin)
