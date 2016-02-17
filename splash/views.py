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
# Create your views here.

    

def index(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        
        form = UserRegistrationForm()
        
    return render(request, "splash/index.html", {'form': form,})
    

def userLogin(request):
    
    email = request.POST['email']
    password = request.POST['password']
    
    #round about way to authenticate with email, by matching email to username.
    #then using the username to authenticate
    # username = User.objects.get(email=email)
    user = authenticate(email=email, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/tasks")
    else:
        return HttpResponseRedirect("/users")