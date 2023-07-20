from django.contrib import admin
from .models import Profile, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

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
          # 'email',
          'phone',
          # 'age',
          'shirt_size',
          'retire_year',
          'bio',
          # 'player_type',
          )
  list_display = ('user',
                  # 'first_name',
                  # 'last_name',
                  'nick_name',
                  # 'email',
                  )

  # ordering=('-nick_name',)


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)