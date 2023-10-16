from django.contrib import admin
from chiya_app.models import product
from django import forms 
class productAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'description')


# Register your models here.
admin.site.register(product, productAdmin)