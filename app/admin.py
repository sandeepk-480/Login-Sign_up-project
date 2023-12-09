from django.contrib import admin
from app.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=('id','first_name', 'last_name', 'email')