from django.db import models

# Create your models here.

class Tujuan(models.Model):
    nama = models.CharField(max_length = 60, default = "")
    img = models.ImageField(upload_to='pics')#where is pics?
    desk = models.CharField(max_length = 100)
    harga = models.IntegerField()
    # specof = models.BooleanField(default = False)