kata = input() #codeforces
jawab = []


for i in kata:
    if(i !='A' and i !='a' and i !='E' and i !='e' and i !='I' and i !='i' and i !='O' and i !='o' and i !='U' and i !='u' and i !='y' and i!='Y'):
        jawab.append('.')
        jawab.append(i)

hasil = ''.join(jawab)

akhir = hasil.lower()
print(akhir)