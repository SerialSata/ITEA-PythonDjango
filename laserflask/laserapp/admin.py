from django.contrib import admin
from .models import Laserapp, Brand


# @admin.register(Laserapp)
class LaserappAdmin (admin.StackedInline):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price')
    model = Laserapp


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [
        LaserappAdmin,
    ]
