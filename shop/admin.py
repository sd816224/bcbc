from django.contrib import admin

# Register your models here.
from .models import Item,Item_images




class ItemAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    prepopulated_fields = {'slug':('title','price')}

admin.site.register(Item,ItemAdmin)
admin.site.register(Item_images)