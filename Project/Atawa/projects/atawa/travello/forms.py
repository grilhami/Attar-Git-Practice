from django import forms


class TujuanForm(forms.Form):
    nama = forms.CharField(max_length = 60)
    img = forms.ImageField()
    desk = forms.CharField(max_length = 120)
    harga = forms.IntegerField()
    # specof = forms.BooleanField()


    