from django.shortcuts import render, redirect

# Create your views here.

#HomePage
def index(request):
    return render(request, 'login.html')

def search(request):
    return render(request, 'search.html')

def logout(request):
    ##put redirect here
    return render(request, 'logout.html')

#Spotify Login
def login(request):
    name = 'user'
    return render(request, 'login.html', {'name':name})

def redir(request):
    return render(request, 'redir.html')