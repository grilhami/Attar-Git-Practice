from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    tujuan = Tujuan.objects.all() 
    return render(request, "index.html", {'tujuan': tujuan})

def tambahTujuan(request):
    print("hello world12345564344")
    if request.method == "POST":
        print("hello world12345564344")
        form = TujuanForm(request.POST, request.FILES)

        if form.is_valid():
            print("berhasil ngevalidasi form")
            nama = request.POST['nama']
            img = request.POST['img']
            desk = request.POST['desk']
            harga = request.POST['harga']
            # specof = request.POST['specof']

            tujuan_baru = Tujuan(nama = nama, img = img, desk = desk, harga = harga)
            tujuan_baru.save()
            return HttpResponse("Tujuan baru telah berhasil ditambahkan")
    else:
        print(request.method)
        form = TujuanForm()
    return render(request, 'tambahTujuan.html', {'form' : form})