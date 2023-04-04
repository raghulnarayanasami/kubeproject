from django.urls import path

from . import views

urlpatterns = [
   path('', views.dashboard, name='dashboard'),
   path('profile_create/', views.profile_create, name='profile_create'),
   path('profile_data/', views.profile_data, name='profile_data'),
]