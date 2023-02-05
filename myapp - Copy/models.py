from django.db import models


class Product(models.Model):
    pro_name = models.CharField(max_length=100)
    unit = models.IntegerField()
    rate = models.IntegerField()
    img = models.ImageField(upload_to='upload', null=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.pro_name
    

class Customer(models.Model):
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Product_list(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    rate = models.IntegerField()
        
    
class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ForeignKey(Product_list, on_delete=models.CASCADE)

    

