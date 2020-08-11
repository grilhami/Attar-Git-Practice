from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftarMobil, name = 'index'),
    path('tambahMobil', views.tambahMobil, name = 'tambahMobil')
]
