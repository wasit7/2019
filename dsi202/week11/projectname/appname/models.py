from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return "%s %s"%(self.first_name, self.last_name)

class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    def __str__(self):
        return "%s %s"%(self.brand,self.model)

class Rent(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    start = models.DateTimeField(auto_now=False, auto_now_add=True)
    stop = models.DateTimeField(auto_now=True, auto_now_add=False)
