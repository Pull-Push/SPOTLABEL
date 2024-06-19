from django.shortcuts import render, redirect

# Create your views here.

#HomePage
def index(request):
    name = 'user'
    return render(request, 'home.html', {'name':name})

#Spotify Login
def login(request):
    name = 'user'
    return render(request, 'login.html', {'name':name})