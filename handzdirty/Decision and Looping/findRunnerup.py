# 5
# 2 3 5 6 6 

# 5

n = input() #5
n = int(n)
isi = input() #2 3 6 6 5 7 6 4
isi = isi.split()
isi = isi[:n] # 2 3 6 6 5

x = 0
for i in isi:
    i = int(i)
    isi[x] = i
    x+=1

setIsi = set(isi)
isi = list(setIsi)
isi.sort() 
isi.reverse()
print(isi[1])

# jawab = list(setIsi)
# print(jawab)
