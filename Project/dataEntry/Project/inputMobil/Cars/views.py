from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def daftarMobil(request):
    mobil = Mobil.objects.all()

    return render(request, "daftarMobil.html", {'mobil': mobil})

def tambahMobil(request):
    if request.method == "POST":
        form = MobilForm(request.POST)

        if form.is_valid():
            merk = request.POST['merk']
            nama = request.POST['nama']
            tahun = request.POST['tahun']
            harga = request.POST['harga']

            mobil_baru = Mobil(merk = merk, nama = nama, tahun = tahun, harga = harga)
            mobil_baru.save()
            return HttpResponse("Mobil baru telah berhasil ditambahkan")
    else:
        form = MobilForm()
    return render(request, 'tambahMobil.html', {'form' : form})