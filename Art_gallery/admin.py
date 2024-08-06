from django.contrib import admin
from Art_gallery.models import Artgallery
# Register your models here.
class new(admin.ModelAdmin):
    list_display=('photo','info')

admin.site.register(Artgallery,new)