from django.contrib import admin

# Register your models here.
# myapp/admin.py
from .models import CustomUser

admin.site.register(CustomUser)
