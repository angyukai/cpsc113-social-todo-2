from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userLogin',views.userLogin, name='userLogin')

]

