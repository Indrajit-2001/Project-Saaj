from django.contrib import admin
from Party_look_gallery.models import Partylookgallery
# Register your models here.
class new(admin.ModelAdmin):
    list_display = ('photo','info')

admin.site.register(Partylookgallery,new)