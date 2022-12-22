from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class chatapp(models.Model):
    participants = ArrayField(models.CharField(max_length=20), default=[], form_size=10, blank=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=False)
    grpadmin_name = models.CharField(max_length=100, blank=False)
    id=models.IntegerField()

    def __str__(self):
        return self.grpadmin_name


    # Username , password , Name , Photo, Phone for register
    # Username , password for Login

