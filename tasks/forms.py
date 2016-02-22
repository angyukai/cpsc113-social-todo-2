from django.forms import ModelForm
from .models import Task
from django import forms

class ValidationError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


class taskForm(forms.Form):
    
	title = forms.CharField(label='title')
	description = forms.CharField(label='description',required=False)

	class Meta:
		model = Task
		
		
		
		
    	
        

	    
	
	
		