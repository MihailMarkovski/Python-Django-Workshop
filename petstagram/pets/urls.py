from django.urls import path

from pets import views



urlpatterns = [
    path('', views.pets_list, name='pets list'),
    path('create/', views.create_pet, name='create pet'),

    path('details/<int:pk>/', views.details_or_comment_pet, name='pet details or comment'),

    path('like/<int:pk>/', views.like_pet, name='like pet'),
    path('edit/<int:pk>/', views.edit_pet, name='edit pet'),
    path('delete/<int:pk>/', views.delete_pet, name='delete pet'),

]
