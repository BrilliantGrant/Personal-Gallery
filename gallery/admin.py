from django.contrib import admin
from .models import Images, Location, categories

class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Images, ImagesAdmin)
admin.site.register(Location)
admin.site.register(categories)
