from django.contrib import admin

# Register your models here.
from .models import home , Category

admin.site.register(home)

admin.site.register(Category)
