from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from splash.models import myUser
# from . import CollabEmails

# Create your models here.

#Do i put my users here?

        
class CollabEmails(models.Model):
    
    email = models.EmailField(max_length = 50)
    def __str__(self):
        return self.email
        
class Task(models.Model):
    owner = models.ForeignKey(myUser, related_name="owned_tasks")
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    collaborators = models.ManyToManyField(CollabEmails)
    isComplete = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.owner
        return self.title
        return self.description
    
    def isCompleteStatus(self):
        return isComplete

