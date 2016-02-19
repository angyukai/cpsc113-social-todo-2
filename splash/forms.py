from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import myUser

# class UserRegistrationForm(forms.Form):
#     """
#     Form for registering a new account.
#     """
#     first_name = forms.CharField(min_length = 1, max_length = 50)
#     last_name = forms.CharField(min_length = 1, max_length = 50)
#     email = forms.EmailField(min_length = 1,max_length = 50,label="Email")
#     password1 = forms.CharField(min_length = 1,max_length = 50)
#     password2 = forms.CharField(min_length = 1,max_length = 50,
#                                 label="Password Confirmation")

#     class Meta:
#         model = User
#         fields = ['first_name','last_name','email', 'password1', 'password2']

#     def clean(self):
#         """
#         Verifies that the values entered into the password fields match

#         NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
#         """
#         cleaned_data = super(UserRegistrationForm, self).clean()
#         if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#             if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#                 raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
#         return self.cleaned_data

#     def save(self, commit=True):
#         user = super(UserRegistrationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         if commit:
#             user.save()
#         return user

class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField(min_length = 1, max_length = 50)
    last_name = forms.CharField(min_length = 1, max_length = 50)
    email = forms.EmailField(required=True)

    class Meta:
        model = myUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        myUser = super(UserRegistrationForm, self).save(commit=False)
        myUser.email = self.cleaned_data['email']
        
        if commit:
            myUser.save()
            
        return myUser