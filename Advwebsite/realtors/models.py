from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    logged_in = models.BooleanField(default=False, blank=False)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=100, blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=False)
    hire_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


    # Username , password , Name , Photo, Phone for register
    # Username , password for Login


