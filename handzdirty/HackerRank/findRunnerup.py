# 5
# 2 3 5 6 6 

# 5

n = input("Input jumlah: ")
x = int(n)


arr = []
for i in range(x):
    angka = input("Input angka: ")
    angka = int(angka)
    arr.append(angka)

a_set = set(arr)
arr2 = list(a_set)
arr2.sort()
arr2.reverse()

print(arr2[1])



# cek_angka = arr[1:]

# curr = arr[1]
# for i in range(len(arr[1:])):
#     if(curr < cek_angka[i]):
#         curr = cek_angka[i]

# if(curr == arr[])