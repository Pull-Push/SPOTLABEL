from django.urls import path
from . import views

urlpatterns = [
    path('', views.vite, name='home'),
    path('log', views.login, name='login'),
    path('redir/', views.redir, name='redir'),
    path('vite', views.vite, name='vite'),
    path('callback', views.callback, name='callback')
]