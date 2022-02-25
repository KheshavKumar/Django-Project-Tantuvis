from django.contrib import admin
from django.urls import path

from accounts.views import register_views

urlpatterns = [
    #path('',index_views, name='home'),
    path('',register_views, name = 'register')
]