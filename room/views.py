from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .form import * 
from .models import * 

def add_category(request):
    categories = Category.objects.filter(user=request.user)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request, 'New category added and saved to Database')
            return redirect('add-category')
        else:
            messages.warning(request, 'Something went wrong. Please try again')
            return redirect('add-category')
    else:
        form = AddCategoryForm()
        context = {'form':form, 'categories':categories}
    return render(request, 'room/add_category.html', context)

def update_category(request, pk):
    category = Category.objects.get(pk=pk)
    categories = Category.objects.filter(user=request.user)
    if request.method == 'POST':
        form = UpdateCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category information updated and saved')
            return redirect(reverse('update-category', args=[category.pk]))
        else:
            messages.warning(request, 'Someting went wrong. Please check form input')
            return redirect(reverse('update-category', args=[category.pk]))
    else:
        form = UpdateCategoryForm(instance=category)
        context = {'form':form, 'categories':categories}
    return render(request, 'room/update_category.html', context)

def add_room(request):
    available_rooms = Room.objects.filter(user=request.user, is_available=True).count()
    booked_rooms = Room.objects.filter(user=request.user, is_available=False).count()
    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request, 'New Room added and saved to Database')
            return redirect('add-room')
        else:
            messages.warning(request, 'Something went wrong. Please try again')
            return redirect('add-room')
    else:
        form = AddRoomForm()
        context = {'form':form, 'available_rooms':available_rooms, 'booked_rooms':booked_rooms}
    return render(request, 'room/add_room.html', context)

def update_room(request, pk):
    rooms = Room.objects.filter(user=request.user)
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category information updated and saved')
            return redirect(reverse('update-room', args=[room.pk]))
        else:
            messages.warning(request, 'Someting went wrong. Please check form input')
            return redirect(reverse('update-room', args=[room.pk]))
    else:
        form = UpdateRoomForm(instance=room)
        context = {'form':form, 'rooms':rooms}
    return render(request, 'room/update_room.html', context)

def book_room(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddBookRoomForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.room = room.pk
            var.save()
            room.is_available= False
            room.save()
            messages.success(request, f'{var.room.name} is booked from {var.start_date} to {var.end_date}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please try again')
            return redirect(reverse('book-room', args=[room.pk]))
    else:
        form = AddBookRoomForm()
        form.fields['room'].queryset = Room.objects.filter(is_available=True)
        context = {'form':form}
    return render(request, 'room/book_room.html', context)

def update_booked_room(request, pk):
    room = BookRoom.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateBookRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booked Room information updated and saved')
            return redirect(reverse('update-booked-room', args=[room.pk]))
        else:
            messages.warning(request, 'Someting went wrong. Please check form input')
            return redirect(reverse('update-room', args=[room.pk]))
    else:
        form = UpdateBookRoomForm(instance=room)
        context = {'form':form}
    return render(request, 'room/update_booked_room.html', context)

def all_booked_rooms(request):
    rooms = Room.objects.filter(user=request.user, is_available=False)
    context = {'rooms':rooms}
    return render(request, 'room/all_booked_rooms.html', context)

def all_available_rooms(request):
    rooms = Room.objects.filter(user=request.user, is_available=True)
    context = {'rooms':rooms}
    return render(request, 'room/all_available_rooms.html', context)

def check_out_guest(request, pk):
    booked_room = BookRoom.objects.get(pk=pk)
    booked_room.has_checked_out = True
    booked_room.save()
    room =Room.objects.get(pk=booked_room.room.pk)
    room.is_available = True
    room.save()
    messages.success(request, 'Guest is now checked out and room is ready again')
    return redirect('dashboard')
