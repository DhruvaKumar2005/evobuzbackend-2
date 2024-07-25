from django.db import models
from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Business_name = models.CharField(max_length=255)
    product_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    

    def __str__(self):
        return self.product_name

class Services(models.Model):
    description_ser = models.CharField(max_length = 300)
    highestAmount = models.DecimalField(max_digits = 10, decimal_places=2)
    location = models.CharField(max_length=50)
    lowestAmount = models.DecimalField(max_digits = 10, decimal_places=2)
    serviceCategory = models.CharField(max_length = 50)
    serviceName = models.CharField(max_length = 50)
    selectedEventTypes = ArrayField(models.CharField(max_length = 50))
    selectedServices = ArrayField(models.CharField(max_length=200))
    images = models.ImageField(upload_to='./media')
    videos = models.FileField(upload_to='./media')

    def __str__(self):
        return self.serviceName


class User(models.Model):
    businessName = models.CharField(max_length=255)
    business_logo = models.ImageField(upload_to='./media')
    owner_name = models.CharField(max_length = 50)
    phone_number = models.DecimalField(max_digits=10, decimal_places= 2)
    gst_number = models.CharField(max_length = 15)
    pan_number = models.CharField(max_length = 10)

    def __str__(self):
        return self.businessName
