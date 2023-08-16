from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name
    
class Laptop(models.Model):
    prodid = models.CharField(max_length=10, primary_key=True)
    brand_name = models.CharField(max_length=20, blank=True)
    model_name = models.CharField(max_length=20, blank=True)
    price = models.FloatField(blank=True, null=True)
    date_of_manf = models.DateField(blank=True, null=True)
    processor = models.CharField(max_length=20, blank=True)
    Storage = models.CharField(max_length=5, blank=True)
    ram = models.CharField(max_length=5, blank=True)
    OS = models.CharField(max_length=30, blank=True)
    size = models.IntegerField(blank=True, null=True)
    screen_type = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.prodid
    
    class Meta:
        db_table='laptop'

class Customer(models.Model):
    custid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    emailid = models.CharField(max_length=30, null=True, blank=True)
    ph_no = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.custid
    
    class Meta:
        db_table='customer'