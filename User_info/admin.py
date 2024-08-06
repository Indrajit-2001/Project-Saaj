from django.contrib import admin
from User_info.models import User_info
# Register your models here.
class new(admin.ModelAdmin):
    list_display=('name','email','phone','date')

admin.site.register(User_info,new)