from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('program/create/', views.create_program, name='create_program'),
    path('client/register/', views.register_client, name='register_client'),
    path('client/enroll/', views.enroll_client, name='enroll_client'),
    path('client/search/', views.search_clients, name='search_clients'),
    path('client/profile/<int:pk>/', views.client_profile, name='client_profile'),
    path('api/client/<int:pk>/', views.client_api, name='client_api'),
  
]