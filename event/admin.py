from django.contrib import admin
from .models import Event
from .models import RSVP_Profile_inter
# Register your models here.
admin.site.register(Event)
# admin.site.register(RSVP_Profile_inter)

# @admin.register(RSVP_Profile_inter)
# class RSVP_Profile_interAdmin(admin.ModelAdmin):
#   fields=('event','profile','RSVP_datetime')
#   list_display = ('Event','Profile','RSVP_datetime')
#   ordering=('-RSVP_datetime',)

@admin.register(RSVP_Profile_inter)
class RSVP_Profile_interAdmin(admin.ModelAdmin):
  fields=('event','profile','RSVP_datetime')
  list_display = ('event','profile','RSVP_datetime')
  ordering=('event','RSVP_datetime',)