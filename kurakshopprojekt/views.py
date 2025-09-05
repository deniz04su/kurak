

from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # home.html сенин башкы бет шаблонуң


def logout_view(request):
    logout(request)
    return redirect('login')  # logout болгондон кийин кайсы бетке жөнөтөсүң

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # логинден кийин кайсы бетке жөнөтөсүң
        else:
            messages.error(request, "Неправильный логин или пароль")
    return render(request, "login.html")  # login.html – сенин шаблон

def index(request):
    return render(request, 'kurakshopprojekt/index.html')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "kurakshopprojekt/register.html", {"form": form})

def profile(request):
    return render(request, "kurakshopprojekt/profile.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('index')  # Тиркеменин башкы бетине жөнөтөт
    return render(request, 'register.html')

