from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True) #auto_now update date all the time when updated
    created = models.DateTimeField(auto_now_add=True)#auto_now_add update the date at 1st time when created
    
    #list the value in decending order with [-] symbol in screen
    class Meta:
        ordering  = ['-updated', '-created']
    

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    # Used django built in table
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #auto_now update date all the time when updated
    created = models.DateTimeField(auto_now_add=True)#auto_now_add update the date at 1st time when created
    
    def __str__(self):
        return str(self.body[0:50])