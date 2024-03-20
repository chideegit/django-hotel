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
    if not request.user.has_hotel:
        if request.method == 'POST':
            form = AddHotelForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.save()

                user = User.objects.get(pk=request.user.pk)
                user.has_hotel = True
                user.save()
                messages.success(request, 'Hotel has been added')
                return HttpResponseRedirect(reverse('hotel-details', args=[form]))
            else:
                messages.warning(request, 'Something went wrong.')
                return redirect('add-hotel')
        else:
            form = AddHotelForm()
            context = {'form':form}
        return render(request, 'hotel/add_hotel.html', context)
    else:
        messages.warning(request, 'You have already added your company')
        return redirect('dashboard')

@login_required
def update_hotel(request):
    hotel = Hotel.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateHotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hotel Info updated')
            return redirect('update-hotel')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('update-hotel')
    else:
        form = UpdateHotelForm(instance=hotel)
        context = {'form':form}
    return render(request, 'hotel/update_hotel.html', context)

@login_required
def hotel_details(request):
    hotel = Hotel.objects.get(user=request.user)
    context = {'hotel':hotel}
    return render(request, 'hotel/hotel_details.html', context)
