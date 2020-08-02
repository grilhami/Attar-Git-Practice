isi = input() 
isi = isi.split()
my_result = []
expected_result = [1, 2, 3, 4, 6, 7, 9]


def ubahKeInt(isi):
    x = 0
    for i in isi:
        i = int(i)
        isi[x] = i
        x+=1
    isi.sort()
    setIsi = set(isi)
    isi = list(setIsi)
    return isi

hasil = ubahKeInt(isi)
my_result = hasil

print(isi)

try:
    assert my_result == expected_result
except:
    print("Tidak sama bro")