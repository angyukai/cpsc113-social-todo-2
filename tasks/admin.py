from django.contrib import admin
from .models import Task
from .models import CollabEmails
from splash.models import myUser



# Register your models here.

admin.site.register(Task)
admin.site.register(CollabEmails)
# admin.site.register(myUser)