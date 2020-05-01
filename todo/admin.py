from django.contrib import admin
from .models import Todo, Todoweekend

# Register your models here.

admin.site.register(Todo)
admin.site.register(Todoweekend)