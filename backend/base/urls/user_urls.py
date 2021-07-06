from django.urls import path, include
from base.views import user_views as views


urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='user-profile'),
    path('', views.getUsers, name='user'),
]
