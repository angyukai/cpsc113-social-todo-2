from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

User._meta.get_field('email')._unique = True
# User.USERNAME_FIELD = 'email'
# Create your models here.

class myUser(AbstractBaseUser):
    """ 
    Custom user with email for authentication
    """
    
    email = models.EmailField('email', unique=True, db_index=True)
    first_name = models.CharField('first_name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    last_name = models.CharField(max_length=50)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __unicode__(self):
        return self.email


