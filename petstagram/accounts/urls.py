from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register user'),
    path('logout/', views.logout_user, name='logout user'),
    path('profile/', views.user_profile, name='current profile user'),
    path('profile/<int:pk>/', views.user_profile, name='profile user'),
]
