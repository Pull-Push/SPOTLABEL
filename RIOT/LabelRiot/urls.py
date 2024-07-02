from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log', views.login, name='login'),
    path('redir/', views.redir, name='redir'),
    path('search', views.search, name='search'),
    path('logout', views.logout, name='logout')
    
]