from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Do i put my users here?


class Task(models.Model):
    owner = models.ForeignKey(User, related_name="owned_tasks")
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    collaborators = models.ManyToManyField(User, related_name="tasks")
    def __str__(self):
        # return self.owner
        return self.title
        return self.description

# class TestQuestion(models.Model):
#     q_text = models.CharField(max_length=500)
#     q_name = models.CharField(max_length=500)
#     def __str__(self):
#         return self.q_text
