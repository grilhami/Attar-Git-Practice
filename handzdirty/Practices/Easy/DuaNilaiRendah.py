# a = True
# while(a):
n = input()
n = int(n)
    # if(n <= 5 & n >=2):
    #     a = False

anak = []
sortNilai = []
jawab = []

for i in range(n):
    nama = input()
    nilai =input()
    nilai = float(nilai)
    anak.append([nama, nilai])

curnil = nilai
for i in anak:
    sortNilai.append(i[1])
sortNilai.sort()
rank1 = sortNilai[0]
rank2 = sortNilai[1]

for i in anak:
    if(i[1] == rank2):
        jawab.append(i[0])
        jawab.sort()

for i in jawab:
    print(i)  