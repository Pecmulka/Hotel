from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .models import Service, Guess, Room, Category, Booking, ServiceProvision


def is_manager(user):
    return user.is_authenticated and user.is_staff


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Неверные учетные данные'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    return render(request, 'home.html')


def services_view(request):
    search_query = request.GET.get('search', '')

    if search_query and request.user.is_staff:
        services = Service.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    else:
        services = Service.objects.all()

    return render(request, 'services.html', {
        'services': services,
        'search_query': search_query,
        'user_role': 'manager' if request.user.is_staff else 'guest'
    })


# Функциональность менеджера
@user_passes_test(is_manager)
def manager_clients_view(request):
    clients = Guess.objects.all()
    return render(request, 'clients.html', {'clients': clients})


@user_passes_test(is_manager)
def manager_rooms_view(request):
    categories = Category.objects.all()
    bed_count = request.GET.get('bed_count', '')
    category_id = request.GET.get('category_id', '')

    rooms = Room.objects.all()

    if bed_count:
        rooms = rooms.filter(bed_count=bed_count)
    if category_id:
        rooms = rooms.filter(category_id=category_id)

    return render(request, 'rooms.html', {
        'rooms': rooms,
        'categories': categories,
        'current_bed_count': bed_count,
        'current_category_id': category_id
    })


@user_passes_test(is_manager)
def manager_book_service_view(request):
    clients = Guess.objects.all()
    services = Service.objects.all()
    bookings = Booking.objects.all()

    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        booking_id = request.POST.get('booking_id')
        count = request.POST.get('count', 1)
        date = request.POST.get('date')

        if service_id and booking_id and date:
            ServiceProvision.objects.create(
                booking_id=booking_id,
                service_id=service_id,
                count=count,
                date=date
            )
            return redirect('manager_book_service')

    return render(request, 'book_service.html', {
        'clients': clients,
        'services': services,
        'bookings': bookings
    })


