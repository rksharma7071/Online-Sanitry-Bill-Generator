from django.contrib import admin
from .models import Product, Customer, Product_list,Bill

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pro_name', 'unit', 'rate', 'category')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'address', 'date')


@admin.register(Product_list)
class Product_listAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'rate')


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('customer', 'products')


