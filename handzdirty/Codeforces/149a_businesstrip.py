max = input() #5 
max = int(max)
isi = input()       #1 1 1 1 2 2 3 2 2 1 1 1
isi = isi.split()
isi = isi[:12] 

x = 0
for i in isi:
    i = int(i)
    isi[x] = i
    x+=1

isi.sort(reverse = True)          #3 2 2 2 2 1 1 1 1 1 1 1

cek = 0
jawab = 0
for i in isi:
    if(max == 0):
        break
    if(max > sum(isi)):
        jawab = -1
        break
    cek = cek + i
    jawab += 1
    if(cek >= max):
        break

print(jawab)