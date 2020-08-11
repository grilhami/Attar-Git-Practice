from django.db import models

# Create your models here.

class Mobil(models.Model):
    merk = models.CharField(max_length = 60)
    nama = models.CharField(max_length = 60)
    tahun = models.IntegerField()
    harga = models.IntegerField()   