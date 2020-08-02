ujian = input() #3
ujian = int(ujian)

nilai = input() # 4 4 4
nilai = nilai.split()
nilai = nilai[:ujian] 

x = 0
for i in nilai: # 4.0 4.0 4.0
    i = float(i)
    nilai[x] = i
    x+=1

ketambah = sum(nilai)   #12.0
rata2 = ketambah / ujian    #12.0 / 3 = 4.0
ulang = 0

print(rata2)
while(rata2 < 4.50): #4.25 < 4.5 T,  4.50 < 4.5
    ujian += 1  #4, 5
    ketambah = ketambah + 5.0   #17.0,  22.0
    rata2 = ketambah / ujian    #17.0 / 4 = 4.25,   22.0 / 5 = 4.50
    ulang += 1                  #1, 2
    print(rata2)

print(ulang)