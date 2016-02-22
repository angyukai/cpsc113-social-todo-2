from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.contrib.auth import logout
from .models import Task
from .models import CollabEmails
from splash.models import myUser
from django import forms
from itertools import chain
from django.db.models import Q
from forms import taskForm
from django.contrib.auth.decorators import login_required
from splash.forms import ValidationError

# Create your views here.


def errors_to_strings(argument):
    switcher = {
        'invalid_email': "Invalid email address",
        'a':'Title too short',
        'b':'Title too long',
        'c':'Description too short',
        'd':'Description too long'
        }
    return switcher.get(argument, argument)

def index(request):
    
    if request.method == 'GET':
		error = request.GET.get('error','')
		error = errors_to_strings(error)
    
    user = request.user
    print user.email
    
    task_list1 = Task.objects.filter(owner=user)
    
    task_list2 = Task.objects.filter(collaborators__email=user.email)
    
    task_list = chain(task_list1,task_list2)
    
    context = {'task_list': task_list, 'task_Form': taskForm, 'error': error}

    template = loader.get_template("tasks/index.html")
    
    return HttpResponse(template.render(context, request))

    
    
    
def userLogout(request):
    logout(request)
    return HttpResponseRedirect("/")
    
def completeTask(request):
    
    print 'hello'
    
    if request.method == 'POST':
        taskId = request.POST['taskId']
  
        task = Task.objects.get(id=taskId)
        # print task
        
        # print ('taskid is..."'+taskId)
    
        if (task.isComplete):
            print 'task is complete'
            task.isComplete = False
            task.save()
        else:
            print 'task is not complete'
            task.isComplete = True
            task.save()
            
    return HttpResponseRedirect("/tasks")
    
def deleteTask(request):
    
    print 'hello im deleting a task'
    
    if request.method == 'POST':
        taskId = request.POST['taskId']
        task = Task.objects.get(id=taskId)
        task.delete()
    return HttpResponseRedirect("/tasks")



@login_required
def createTask(request):
    
    if request.method == 'POST':
        
        
        collab1 = CollabEmails(email = request.POST['collab1'])
        collab1.save()
        collab2 = CollabEmails(email = request.POST['collab2'])
        collab2.save()
        collab3 = CollabEmails(email = request.POST['collab3'])
        collab3.save()

        form = taskForm(request.POST)
        
        if form.is_valid():
            
            try:

                data = form.cleaned_data
                
                title = data['title']
                desc = data ['description']
                
                if len(title) < 1:
                    raise ValidationError('a')
                elif len(title) > 500:
                    raise ValidationError('b')
                
                if len(desc) < 1:
                    raise ValidationError('c')
                elif len(desc) > 5000:
                    raise ValidationError('d')
                
                task = Task(owner = request.user, title = data['title'], description = data['description'])
                task.save()
                
                
                task.collaborators.add(collab1)
                task.collaborators.add(collab2)
                task.collaborators.add(collab3)

                task.save()
                return HttpResponseRedirect('/tasks')
                
            except Exception as error:
                return HttpResponseRedirect('/tasks?error='+str(error)[1:-1])
            return HttpResponseRedirect('/tasks')
            
        return HttpResponseRedirect('/tasks?error=invalid_input')
    return HttpResponse(403)
        
    
    
    
def detail(request, task_id):
    
    return HttpResponse("You're looking at task %s." % task_id)