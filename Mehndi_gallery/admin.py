from django.contrib import admin
from Mehndi_gallery.models import Mehndigallery
# Register your models here.
class new(admin.ModelAdmin):
    list_display=('photo','info')

admin.site.register(Mehndigallery,new)