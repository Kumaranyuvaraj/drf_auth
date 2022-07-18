from django.urls import path
from authent.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView,GetView,GetListView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import views

from .views import (ListCategory, DetailCategory,ListSubCategory,DetailSubCategory, 
                    ListProduct, DetailProduct, ListUser, 
                    DetailUser, ListCart, DetailCart)



urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', views.ChangePasswordView, name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('getDetails/',GetView.as_view()),
    path('getDetails/<int:id>/',GetListView.as_view()),
    # path('change_password/<int:pk>/',ChangePasswordView.as_view()),
    
    
    path('categories/', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    
    path('sub_categories/', ListSubCategory.as_view(), name='sub_categorie'),
    path('sub_categories/<int:pk>/', DetailSubCategory.as_view(), name='singlesub_category'),
    
    # path('books/', ListBook.as_view(), name='books'),
    # path('books/<int:pk>/', DetailBook.as_view(), name='singlebook'),

    path('products/', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('users/', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),

    path('carts/', ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', DetailCart.as_view(), name='cartdetail'),
    
]

