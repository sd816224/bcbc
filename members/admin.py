from django.contrib import admin
from .models import Profile
# Register your models here.
# admin.site.register(MemberType)
# admin.site.register(Profile)


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  fields=('user',
          'first_name',
          'last_name',
          'nick_name',
          'email',
          'phone',
          'age',
          'shirt_size',
          'bio',
          'player_type',
          )
  list_display = ('user',
                  'first_name',
                  'last_name',
                  'nick_name',
                  'email',
                  )
  ordering=('-nick_name',)