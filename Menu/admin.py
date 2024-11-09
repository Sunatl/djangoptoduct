from django.contrib import admin
from .models import *

@admin.register(Product)
class Pr(admin.ModelAdmin):
    list_display = ("name","price","stock")
    search_fields = ("name","price","stock")
    list_filter = ("name","price","stock")
    

@admin.register(Customer)
class Cas(admin.ModelAdmin):
    list_display = ("name","email","phone_number")
    search_fields =("name","email","phone_number")
    list_filter = ("name","email","phone_number")
    
@admin.register(Order)
class Or(admin.ModelAdmin):
    list_display = ("customer","product","quantity")
    search_fields =("customer__name","product__name","quantity")
    list_filter = ("customer","product","quantity")
    