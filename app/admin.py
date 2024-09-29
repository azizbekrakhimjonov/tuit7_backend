from django.contrib import admin
from .models import *

# Register your models here.


from django.contrib import admin

admin.site.register(Bino)
@admin.register(Universitet)
class UniversitetAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'manzil', 'asos_sanasi', 'rektor', 'xorij_hamkorlik', 'contact','davlat')  # davlat maydoniga ishora
    list_filter = ('davlat',)  # davlat maydoniga ishora
