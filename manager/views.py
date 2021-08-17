from django.shortcuts import render, HttpResponse, redirect
from manager.models import User, Project, Message, Task
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'register.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if request.method == 'POST':
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        User.register(request.POST)
    return redirect('/')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/dashboard')
    return redirect('/')

def dashboard(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    projects = Project.objects.filter(contributor=logged_user)
    context = {
        'user_projects' : projects
    }
    return render(request, 'dashboard.html', context)

def create_project(request):
    context = {
        'contributors' : User.objects.all()
    }
    return render(request, 'create_project.html', context)

def project_creation(request):
    new_project = Project.objects.create(title=request.POST['title'], due_on=request.POST['due_on'], contributor=User.objects.get(id =request.POST['contributors']), projectManager=User.objects.get(id=request.session['user_id']))
    request.session['project_id'] = new_project.id
    return redirect('create/task')

def create_task(request):
    context = {
        'contributors' : User.objects.all()
    }
    return render(request, 'create_task.html', context)

def task_creation(request):
    Task.objects.create(task = request.POST['task'], due_on = request.POST['due_on'], assigned_to = User.objects.get(id=request.POST['contributors']), project = Project.objects.get(id=request.session['project_id']))
    return redirect('create/task')

def inbox(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    sent_messages = Message.objects.filter(reciever=logged_user)
    context = {
        'inbox' : sent_messages
    }
    return render(request, 'inbox.html', context)

def message(request, message_id):
    message = Message.object.get(id=message_id)
    context = {
        'user_message': message
    }
    return render(request, 'message.html', context)

def new_message(request):
    return render(request, 'new_message.html')

def project(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {
        'user_project' : project
    }
    return render(request, 'view_project', context)

