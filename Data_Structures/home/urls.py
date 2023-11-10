from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
   path('', views.home, name='home'),
   path('addcontact', views.addcontact, name='addcontact'),
   path('dltcontact', views.dltcontact, name='dltcontact'),
   path('search', views.search, name='search'),
   path('modify', views.modify, name='modify'),
   path('contactlist', views.contactlist, name='contactlist')
   
]