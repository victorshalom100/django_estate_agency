from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('edit/<int:listing_id>', views.edit, name='edit'),
    path('logout', views.my_logout, name='logout'),
    path('profile/', views.settings, name="settings"),
    path('settings/', views.profile, name="profile"),
    path('msg/', views.msg, name="msg")

    
]