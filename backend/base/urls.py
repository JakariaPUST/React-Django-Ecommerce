from django.urls import path, include
from . import views


urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('', views.getRoutes, name='routes'),
    path('products/', views.getproducts, name='products'),
    path('products/<str:pk>/', views.getproduct, name='product'),
]
