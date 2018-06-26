from django.conf.urls import patterns, url

from feeds import views

urlpatterns = patterns('',
   url(r'^add', views.add, name='add'),
   url(r'^del', views.delete, name='delete'),
   url(r'^list', views.list, name='list'),
   url(r'^$', views.index, name='index')
)
