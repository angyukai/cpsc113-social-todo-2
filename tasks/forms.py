from django.forms import ModelForm
from .models import Task
from django import forms

class taskForm(ModelForm):
    
    title = forms.CharField(min_length = 1, max_length = 50)
    description = forms.CharField(min_length = 1, max_length = 50)

    class Meta:
        model = Task
        fields = ['title','description']
        
    # def save(self, user, commit=True):
    #     Task = super(taskForm, self).save(commit=False)
    #     Task.owner = user
    #     # Task.description = self.cleaned_data['description']
    #     # Task.collaborators = self.cleaned_data['collaborators']
        
    #     if commit:
    #         Task.save()
        
    #     return Task