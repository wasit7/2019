from django.db import models

class Customer(models.Model):
    firstname = models.CharField( max_length=50 )
    lastname = models.CharField( max_length=50 )
    dob = models.DateField()
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Transaction(models.Model):
    datetime = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.datetime}.{self.customer}"

class Item(models.Model):
    name = models.CharField( max_length=20 )
    price = models.DecimalField( max_digits=10, decimal_places=2 )
    def __str__(self):
        return f"{self.name} {self.price}"

class Record(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)