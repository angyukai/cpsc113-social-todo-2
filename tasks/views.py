from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.contrib.auth import logout
from .models import Task
from .models import CollabEmails
from splash.models import myUser

from itertools import chain
from django.db.models import Q
from forms import taskForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    
    user = request.user
    print user.email
    
    task_list1 = Task.objects.filter(owner=user)
    
    task_list2 = Task.objects.filter(collaborators__email=user.email)
    
    task_list = chain(task_list1,task_list2)
    
    context = {'task_list': task_list, 'task_Form': taskForm}

    template = loader.get_template("tasks/index.html")
    
    return HttpResponse(template.render(context, request))

    
    
    
def userLogout(request):
    logout(request)
    return HttpResponseRedirect("/")
    
def completeTask(request):
    
    print 'hello'
    
    if request.method == 'POST':
        taskId = request.POST['taskId']
        
        # isComplete = request.post.isComplete
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

# def createTask(request):
    
#     print 'hello im creating a task'
    
#     if request.method == 'POST':
        
#         email = request.POST['email']
#         owner = myUser.objects.get(email=email)
#         title = request.POST['title']
#         description = request.POST['description']
#         collab1 = request.POST['collaborator1']
#         collab2 = request.POST['collaborator2']
#         collab3 = request.POST['collaborator3']
#         collabs = [collab1,collab2,collab3]
        
        
        
#         task = Task(owner = owner, title = title, description = description)
#         task.save()
        
#     return HttpResponseRedirect("/tasks")

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
            
            
            
            # collabs = [collab1, collab2, collab3]
            
            # for c in collabs:
            #     print c
            
            print collab1
            print collab2
            print collab3
            
            data = form.cleaned_data
            task = Task(owner = request.user, title = data['title'], 
            description = data['description'])
            task.save()
            
            # print task.owner
            
            task.collaborators.add(collab1)
            task.collaborators.add(collab2)
            task.collaborators.add(collab3)
            # for c in collabs:
            #     task.collaborators.add(c)
            task.save()
            # user = request.user
            # new_task = form.save(form, user)
            # return HttpResponseRedirect("/tasks")
            
    else:
        
        form = taskForm()
        
    return HttpResponseRedirect('/tasks')
    
    
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")
    
    
def detail(request, task_id):
    
    return HttpResponse("You're looking at task %s." % task_id)