from django import forms
from .models import Product, Customer, Product_list, Bill

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ("pro_name", "unit", "amount", "img", "category")


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields = ("name", "email", "mobile", "address", "date", "payment")


class Product_listForm(forms.ModelForm):
    class Meta:
        model = Product_list 
        fields = ('customer', 'product', 'quantity')


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill 
        fields = ('customer', 'products')