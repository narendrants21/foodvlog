from django.contrib import admin
from.models import *
# Register your models here.
class catagdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Categ,catagdmin)

class prodadmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'img','available']
    list_editable = ['price', 'stock', 'img','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product, prodadmin)