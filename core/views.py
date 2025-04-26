from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Client, HealthPrograme, Enrollment
from .forms import RegistrationForm,ClientForm, HealthProgrameForm, EnrollmentForm
from .serializers import ClientSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    total_clients = Client.objects.count()
    total_programs = HealthPrograme.objects.count()
    total_enrollments = Enrollment.objects.count()

    return render(request, 'dashboard.html', {
        'total_clients': total_clients,
        'total_programs': total_programs,
        'total_enrollments': total_enrollments,
    })
    clients = Client.objects.all()
    programs = HealthPrograme.objects.all()
    enrollments = Enrollment.objects.all()
    return render(request, 'dashboard.html', {'clients': clients, 'programs': programs, 'enrollments': enrollments})
@login_required
def create_program(request):
    if request.method == 'POST':
        form = HealthProgrameForm(request.POST )
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HealthProgrameForm()
    
    programs = HealthPrograme.objects.all()
    return render(request, 'create_program.html', 
                  {'form': form,
                   'programs':programs,})

@login_required
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})

@login_required
def enroll_client(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EnrollmentForm()
    return render(request, 'enroll_client.html', {'form': form})

@login_required
def search_clients(request):
    query = request.GET.get('q')
    clients = Client.objects.filter(first_name__icontains=query) if query else Client.objects.all()
    return render(request, 'search_client.html', {'clients': clients})

@login_required
def client_profile(request, pk):
    client = get_object_or_404(Client, pk=pk)
    enrollments = Enrollment.objects.filter(client=client)
    return render(request, 'client_profile.html', {'client': client, 'enrollments': enrollments} )

#API
@api_view(['GET'])
def client_api(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)