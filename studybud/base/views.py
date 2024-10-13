from django.shortcuts import render
# from django.http import HttpResponse
from .models import Room

# Create your views here.

# def home(request):
#     return HttpResponse("Home Page")

# def room(request):
#     return HttpResponse("Room Page")

# rooms = [
#     {'id':1, 'name':'Lets learn Python'},
#     {'id':2, 'name':'Lets learn django'},
#     {'id':3, 'name':'Design with me'},
# ]

def home(request):
    #will take data from data base
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id = pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
