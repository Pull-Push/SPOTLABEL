from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('log', views.login, name='login')
]