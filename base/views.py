from django.shortcuts import render
from .models import Room, Message

# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

def room(request, id):
    room = Room.objects.get(id=id)
    messages = Message.objects.filter(room=id)
    context = {
        'room': room,
        'messages': messages
    }
    return render(request, 'base/room.html', context)

def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)