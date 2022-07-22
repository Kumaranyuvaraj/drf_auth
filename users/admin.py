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
    

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display =  ('product_tag','name','category','sub_category',
                     'price','stock','imageUrl','created_by','status',
                     'date_created')
    
    list_filter = ('product_tag','name')
    search_fields = ('product_tag','name')
    fieldsets = (
        (None, {
            "fields": ('name','category','sub_category','status'),
            }
         ),
        )
    
    
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            "fields": ('title',),
        }),
    )
    
    
class SubCategoriesAdmin(admin.ModelAdmin):
    model = SubCategory
    list_display = ('productType','category')
    list_filter = ('productType',)
    search_fields = ('productType',)
    fieldsets = (
        (None, {
            "fields": ('category',),
        }),
    )
    

class CartAdmin(admin.ModelAdmin):

    model = Cart
    list_display = ('cart_id','created_at','getProducts')
    list_filter = ('cart_id','created_at')
    search_fields = ['cart_id']
    
    def getProducts(self,obj):
        return "\n".join([p.product_tag for p in obj.products.all()])
    
    fieldsets = (
        (None, {
            "fields": ('products',),
        }),
    )
    
    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoriesAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(User,UserAdmin)
