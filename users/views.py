from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import loader


# Create your views here.

def home(request):
    return HttpResponse('im in user homepage')
    

    