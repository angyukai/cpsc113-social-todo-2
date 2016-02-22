from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userLogout', views.userLogout, name='userLogout'),
    
    
    url(r'^completeTask', views.completeTask, name='completeTask'),
    
    url(r'^deleteTask', views.deleteTask, name='deleteTask'),
    
    url(r'^createTask', views.createTask, name='createTask'),
    url(r'up', views.say_whatsup, name='whatsup'),
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail')
]

