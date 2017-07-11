from django.contrib import admin
from .models import Laserapp


@admin.register(Laserapp)
class LaserappAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price')
