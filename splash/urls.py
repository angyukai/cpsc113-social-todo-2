from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/login',views.userLogin, name='userLogin'),
    url(r'^user/register',views.userRegistration, name='userRegistration')
]

