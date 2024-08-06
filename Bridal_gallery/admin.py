from django.contrib import admin
from Bridal_gallery.models import Bridalgallery
# Register your models here.
class new(admin.ModelAdmin):
    list_display=('photo','info')

admin.site.register(Bridalgallery,new)