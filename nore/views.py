from django.shortcuts import render, get_object_or_404, redirect
from .forms import RoomForm
from .models import Room

# Create your views here.
def list(request):
    rooms = Room.objects.all
    return render(request, 'list.html', {'rooms': rooms})

def show(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'show.html', {'room': room})

def new(request):
    return render(request, 'new.html')

def roomcreate(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('list')
    else:
        form = RoomForm()
        return render(request, 'new.html', {'form': form})