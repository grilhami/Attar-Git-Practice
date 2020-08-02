class MainKurang:
    
    def __init__(self, nama, no1, no2):
        self.nama = nama
        self.no1 = no1
        self.no2 = no2

    def __sub__(self, lain):
        return self.no2 - lain.no2

angka1 = MainKurang("angka hoki",9, 6)
angka2 = MainKurang("angka sial", 8, 4)

hasil = angka1 - angka2
print(hasil)