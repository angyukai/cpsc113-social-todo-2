from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
# User.USERNAME_FIELD = 'email'
# Create your models here.
