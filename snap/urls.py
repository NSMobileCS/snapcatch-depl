from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login/?', views.login),   
    url(r'^home/?$', views.main),
    url(r'^display/?$',views.display),
    url(r'^caught/?$', views.catch), 
]
