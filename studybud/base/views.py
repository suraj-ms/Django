from django.shortcuts import render, redirect
from django.db.models import Q
# from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    #will take data from data base
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(desc__icontains=q) 
        )
    topics = Topic.objects.all()

    room_count = rooms.count()
    context = {'rooms':rooms, 'topics':topics, 'room_count':room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id = pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    
    if request.method=='POST':
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method=='POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html',context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html',{'obj':room})