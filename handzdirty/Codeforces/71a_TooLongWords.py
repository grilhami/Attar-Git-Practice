a = input() #4
a = int(a)
isi = []
jawab = []

for i in range(a):
    kata = input() #word, localization, internationalization, pneumonoultramicroscopicsilicovolcanoconiosis
    isi.append(kata)

y=0
for i in range(a):
    if(len(isi[y]) > 10):
        tengah = len(isi[y][1:-1])
        tengah = str(tengah)
        tambah = isi[y][0] + tengah + isi[y][-1]
        jawab.append(tambah)
    else:
        jawab.append(isi[y])
    y+=1

for i in jawab:
    print(i)