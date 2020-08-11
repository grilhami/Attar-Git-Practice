from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adding', views.tambah, name='tambah')
]