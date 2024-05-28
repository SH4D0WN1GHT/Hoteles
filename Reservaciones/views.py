from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ReservacionForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'prompt': 'Username already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, 'prompt': 'Passwords do not match'})
        
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def main(request):
    return render(request, 'base.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def contacto(request):
    return render(request, 'contacto.html')

def crear_reservacion(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a una lista de reservaciones o una página de éxito
    else:
        form = ReservacionForm()
    return render(request, 'registro.html', {'form': form})
