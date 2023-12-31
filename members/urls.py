"""bcbc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('user_register/', views.user_register,name='user_register'),
    path('user_login/', views.user_login,name='user_login'),
    path('user_logout/', views.user_logout,name='user_logout'),
    path('user_profile/', views.user_profile,name='user_profile'),
    path('update_profile/<profile_id>/', views.update_profile,name='update_profile'),
    path('other_profile/<profile_id>/', views.other_profile,name='other_profile'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('test/', views.test,name='test'),
]
