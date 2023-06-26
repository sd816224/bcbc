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
    path('', views.home,name='home'),
    path('contact/', views.contact,name='contact'),
    path('all_venues/', views.all_venues,name='all_venues'),
    path('add_venue/', views.add_venue,name='add_venue'),
    path('all_events/', views.all_events,name='all_events'),
    path('add_event/', views.add_event,name='add_event'),
    path('update_event/<event_id>', views.update_event,name='update_event'),
    path('event_detail/<event_id>/', views.event_detail,name='event_detail'),
    # path('event_detail/<event_id>/<user_id>/', views.add_RSVP,name='add_RSVP'),


]
