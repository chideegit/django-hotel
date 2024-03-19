from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .form import * 
from .models import * 
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def add_hotel(request):
    if request.method == 'POST':
        form = AddHotelForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request, 'Hotel has been added')
            return HttpResponseRedirect(reverse('hotel-details', args=[form]))
        else:
            messages.warning(request, 'Something went wrong.')
            return redirect('add-hotel')
    else:
        form = AddHotelForm()
        context = {'form':form}
    return render(request, 'hotel/add_hotel.html', context)

@login_required
def update_hotel(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateHotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hotel Info updated')
            return HttpResponseRedirect(reverse('hotel-details', args=[hotel.pk]))
        else:
            messages.warning(request, 'Something went wrong')
            return HttpResponseRedirect(reverse('update-hotel', args=[hotel.pk]))
    else:
        form = UpdateHotelForm(instance=hotel)
        context = {'form':form}
    return render(request, 'hotel/update_hotel.html', context)

@login_required
def hotel_details(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    context = {'hotel':hotel}
    return render(request, 'hotel/hotel_details.html', context)
