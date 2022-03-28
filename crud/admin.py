from django.contrib import admin
from .models import Leads, Image
# Register your models here.

class LeadsAdmin(admin.ModelAdmin):

    list_display = ['name', 'phone', 'email', 'designation']

class ImageAdmin(admin.ModelAdmin):

    list_display = ['caption', 'photo']

admin.site.register(Leads, LeadsAdmin)
admin.site.register(Image, ImageAdmin)