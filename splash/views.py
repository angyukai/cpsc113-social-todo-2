from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import myUser
from tasks.forms import ValidationError
# Create your views here.


def errors_to_strings(argument):
    switcher = {
        'invalid_email': "Invalid email address",
        'name_too_short': "name too short",
        'name_too_long': "name too long",
        'email_too_short': "email too short",
        'email_too_long': "email too long",
        'pw_too_short': "password too short",
        'pw_too_long': "password too long",
        'user_exists': "Account with this email already exists!",
        'invalid_password': "Invalid password",
        'invalid_input' : "Please fill in all required fields",
        'passwords_match_fail' : "Passwords don't match"
    }
    return switcher.get(argument, argument)
    

def index(request):
    
    if request.method == 'GET':
		error = request.GET.get('error','')
		error = errors_to_strings(error)
        
    return render(request, "splash/index.html", {'form': UserRegistrationForm, 'error':error})

    

def userLogin(request):
    
    username = request.POST['email']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("/tasks")
    else:
        
		return HttpResponseRedirect('/?error=invalid_password')
    return HttpResponse('lolhello')
    

def userRegistration(request):
    
    if request.method == 'POST':
        
        form = UserRegistrationForm(request.POST)
        # try:
        if form.is_valid():
            try:
                user = form.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return HttpResponseRedirect("/tasks")
            except Exception as error:
                return HttpResponseRedirect('/?error='+str(error)[1:-1])
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/?error=invalid_input')
	return HttpResponse(403)
            

        
    
    