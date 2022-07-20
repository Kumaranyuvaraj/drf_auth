from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
    
class SubCategory(models.Model):
    productType = models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name='sub_category', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'SubCategories'
    def __str__(self):
        return self.productType
    
    
class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,related_name='product',on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # books = models.ManyToManyField(Book)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id', '-created_at']
        

    def __str__(self):
        return f'{self.cart_id}'
    
#######################################################################
# django-admin User Model Customize


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'),max_length=50,null=True,unique=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

   
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email   

