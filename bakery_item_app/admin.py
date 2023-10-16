from django.contrib import admin
from bakery_item_app.models import bakery

# Register your models here.

class bakeryAdmin(admin.ModelAdmin):
    list_display=('name','price','description')

admin.site.register(bakery,bakeryAdmin)