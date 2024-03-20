from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import * 

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = var.email
            var.save()
            messages.success(request, 'Account created. Please log in')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request, 'accounts/register.html', context)

def login_user(request):
    next = ''

    if request.GET:
        next = request.GET['next']

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if next == '':
                messages.success(request, f'You are logged in as {user.first_name}')
                return redirect('dashboard')
            else:
                return redirect(next)
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Your active session has ended')
    return redirect('login')
