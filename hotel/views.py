from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Service

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def guest_services_view(request):
    services = Service.objects.all()
    return render(request, 'guest_services.html', {'services': services})

@login_required
def home_view(request):
    return render(request, 'home.html')

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

