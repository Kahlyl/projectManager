from django.contrib import messages
from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('create_project', views.create_project),
    path('project_creation', views.project_creation),
    path('create/task', views.create_task),
    path('task_creation', views.task_creation),
    path('inbox', views.inbox),
    path('message/<int:message_id>', views.message),
    path('message/new', views.new_message),
    path('project/<int:project_id>', views.project),
    
]