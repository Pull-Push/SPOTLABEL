from django.shortcuts import render, redirect

# Create your views here.

#HomePage
def index(request):
    name = 'user'
    return render(request, 'login.html', {'name':name})

#Spotify Login
def login(request):
    name = 'user'
    return render(request, 'login.html', {'name':name})

def redir(request):
    return render(request, 'redir.html')