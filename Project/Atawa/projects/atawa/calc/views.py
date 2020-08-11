from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Attar'})

def tambah(request):
    jum1 = request.GET['angka1']
    jum2 = request.GET['angka2']
    jum1 = int(jum1)
    jum2 = int(jum2)
    jaw = jum1 + jum2

    return render(request, 'hasil.html', {'jawaban':jaw, 'isirequest':request})