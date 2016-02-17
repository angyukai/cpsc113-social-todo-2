from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import UserRegistrationForm
# Create your views here.


# Create your views here.

# def index(request):
#     return render(request, 'splash/index.html')
    

def index(request):
    
    
    
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserRegistrationForm()
    return render(request, "splash/index.html", {'form': form,})