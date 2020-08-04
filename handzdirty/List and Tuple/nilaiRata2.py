# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# 56.00

try:
    n = input() # 3
    n = int(n)
except:
    print("Harus masukin angka")
    # raise ValueError("Harus masukin angka")

daftarAnak = []
hasilAnak = []


x=0
z=1
try:
    for i in range(n):      
        anak = input()      # 'Krishna' '67' '68' '69'
        anak = anak.split()

        for t in anak[1:]:
            t = int(t)      # 'Krishna' 67 68 69
            anak.append(t)
            del anak[1:2]
except:
    print("Rangenya bukan angka gegara di paling awal")

try:
    daftarAnak.append(anak)
except:
    print("Tidak ada anak")
# print(daftarAnak)

pilih = input() # 3

sum=0
for i in daftarAnak:
    if pilih in i:
        for y in anak[1:]:
            sum += y
        sum /= 3

print(round(sum, 2))
