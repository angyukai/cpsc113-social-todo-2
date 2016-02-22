from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import myUser
from django.core.exceptions import ValidationError


class ValidationError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)




# class UserRegistrationForm(UserCreationForm):

#     fl_name = forms.CharField(min_length = 1, max_length = 50)
#     # last_name = forms.CharField(min_length = 1, max_length = 50)
#     email = forms.EmailField(required=True)
#     # password1 = forms.CharField(widget=forms.HiddenInput())
#     # password2 = forms.CharField(widget=forms.HiddenInput())
    
#     # set_field_html_name(first_name, 'fl_name')

#     class Meta:
#         model = myUser
#         fields = ('fl_name','email','password1','password2')
    
#     def save(self, commit=True):
#         myUser = super(UserRegistrationForm, self).save(commit=False)
#         myUser.email = self.cleaned_data['email']
        
#         if commit:
#             myUser.save()
            
#         return myUser
        
        
class UserRegistrationForm(forms.Form):
    
	fl_name = forms.CharField(label='First and last name')
	email = forms.EmailField(label='email')
	password = forms.CharField(label='password', widget=forms.PasswordInput())
	password_confirmation = forms.CharField(label='password confirmation', widget=forms.PasswordInput())

	class Meta:
		model = myUser

	def save(self):
		data = self.cleaned_data

		_name = data['fl_name']
		if len(_name) == 0:
			raise ValidationError('name_too_short')
		elif len(_name) > 30:
			raise ValidationError('name_too_long')

		_email = data['email']
		if len(_email) < 1:
			raise ValidationError('email_too_short')
		elif len(_email) > 30:
			raise ValidationError('email_too_long')
		elif myUser.objects.filter(email = _email):
			raise ValidationError('user_exists')
			
		_fl_name = _name
		_email = _email
		
		_pw = data['password']
		if len(_pw) < 1:
			raise ValidationError('pw_too_short')
		elif len(_pw) > 30:
			raise ValidationError('pw_too_long')
		_pw2 = data['password_confirmation']
		if _pw != _pw2:
			raise ValidationError('passwords_match_fail')
			
		user = myUser(fl_name=_fl_name, email=_email, password=_pw)
		user.save()
		
		return user
        




# class UserRegistrationForm(UserCreationForm):

#     first_name = forms.CharField(max_length = 50)
    
#     set_field_html_name(first_name, 'fl_name')
    
#     last_name = forms.CharField(max_length = 50)
    
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = myUser
#         fields = ('first_name','last_name','email', 'password1', 'password2')
        
        
#     def save(self, commit=True):
#         myUser = super(UserRegistrationForm, self).save(commit=False)
#         myUser.email = self.cleaned_data['email']
#         # myUser.set_password(self.cleaned_data["password1"])
        
#         if commit:
#             myUser.save()
            
#         return myUser