from django import forms


class MobilForm(forms.Form):
    merk = forms.CharField(max_length = 60)
    nama = forms.CharField(max_length = 60)
    tahun = forms.IntegerField()
    harga = forms.IntegerField()