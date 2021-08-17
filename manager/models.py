from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
import re
import bcrypt

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name needs a minimum of 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name needs a minimum of 2 characters'
        if len(postData['job']) < 2:
            errors['job'] = 'Job needs a minimum of 5 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        email_check = User.objects.filter(email=postData['email'])
        if email_check:
            errors['duplicate_email'] = 'This email is already in use.'
        if postData['password'] != postData['confirm_pw']:
            errors['no_match'] = 'Passwords do not match.'
        else:
            errors['successful'] = 'Registration Successful!!'
        return errors


class User(models.Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    job = CharField(max_length=20)
    email = CharField(max_length=70)
    password = CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def register(postData):
        password = postData['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'],job=postData['job'], password=pw_hash)


    # Message needs to be stored. Need to set a relationship with Owner and Contributor. Owner needs to be able to see all Contributors in the list. Needs to be able to select that Contributor. After selection have a text box to type message(either have a fcn for the Owner to send a message or create a Message object). Send button (need a fcn called CreatMessage(), in there have Owner.objects.createMessage(have who created this message, the message, and who it is being sent to). Load this onto an HTML page for the Contributor to see.). 
class Message(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    sender = models.OneToOneField(User, on_delete=CASCADE)
    reciever = models.ForeignKey(User, related_name='message_sent_to', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    title = models.CharField(max_length=20)
    due_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    projectManager = models.ForeignKey(User,related_name='projectManager', on_delete=CASCADE)
    contributor = models.ForeignKey(User,related_name='projects', on_delete=CASCADE)
    # add a completed function
    #add a function that says what % of tasks done
    #add a function that determines if completed on time and if not how late it is

class Task(models.Model):
    task = models.CharField(max_length=255)
    due_on = models.DateField()
    assigned_to = models.ForeignKey(User, related_name='user_tasks', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, related_name='project_tasks', on_delete=CASCADE)
    # add a report function
    # add a completed function
    #add a function that determines if completed on time and if not how late it is

class Report(models.Model):
    report = models.TextField()
    reporter = OneToOneField(User, on_delete=CASCADE)
    task = OneToOneField(Task, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)