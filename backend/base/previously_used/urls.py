from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/profile/', views.getUserProfile, name='user-profile'),
    path('users/', views.getUsers, name='user'),
    path('products/', views.getproducts, name='products'),
    path('products/<str:pk>/', views.getproduct, name='product'),
]
