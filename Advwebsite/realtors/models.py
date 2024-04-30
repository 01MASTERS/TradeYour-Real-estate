from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Realtor(AbstractUser):
    name = models.CharField(max_length=100, blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=100, blank=False)
    hire_date = models.DateField(default=datetime.now, blank=True)
    
    # Add unique related_name for groups field
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='realtor_groups'
    )

    # Add unique related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='realtor_user_permissions'
    )

    def __str__(self):
        return self.name


    # Username , password , Name , Photo, Phone for register
    # Username , password for Login


