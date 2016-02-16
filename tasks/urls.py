from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'up', views.say_whatsup, name='whatsup'),
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail')
]

