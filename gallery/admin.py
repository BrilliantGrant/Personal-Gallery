from django.contrib import admin
from .models import Photos, Location, categories

class PhotosAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Photos, PhotosAdmin)
admin.site.register(Location)
admin.site.register(categories)
