from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import loader
from .models import Task

# Create your views here.

# def home(request):
    # return HttpResponse("Hi you're at the home page")
    
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#         else:
#             # Return a 'disabled account' error message
#             ...
#     else:
#         # Return an 'invalid login' error message.
#         ...

def index(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    template = loader.get_template("tasks/index.html")
    return HttpResponse(template.render(context, request))
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")
    
    
def detail(request, task_id):
    
    return HttpResponse("You're looking at task %s." % task_id)