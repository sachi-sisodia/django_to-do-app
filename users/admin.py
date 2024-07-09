from django.contrib import admin

# Register your models here.
from users.models import CustomUser

# admin.site.register(CustomUser)



@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=('username','name','email','password')