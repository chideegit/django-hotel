from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect

User = get_user_model()

def check_for_hotel(view_func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if not user.has_hotel:
            return redirect('add-hotel')
        response = view_func(request, *args, **kwargs) 
        return response
    return wrapper