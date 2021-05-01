from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import MyUserCreationForm
from accounts.models import Profile

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.save()
            Profile.objects.create(user=user)
            return redirect('webapp:home')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})