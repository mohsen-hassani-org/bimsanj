from django.contrib import admin
from .models import Career, CareerGroup

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(CareerGroup)
class CareerGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
