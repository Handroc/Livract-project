from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileEditForm
from .models import Profile, Follow


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/login.html', {'error': 'Identifiants incorrects'})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'profile': request.user.profile})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'accounts/profile_edit.html', {'form': form})


@login_required
def follow(request, user_id):
    target = get_object_or_404(User, id=user_id)
    if target != request.user:
        existing = Follow.objects.filter(follower=request.user, followed=target)
        if existing.exists():
            existing.delete()
        else:
            Follow.objects.create(follower=request.user, followed=target)
    return redirect('profile')
