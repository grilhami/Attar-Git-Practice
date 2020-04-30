# 5
# 2 3 6 6 5

# 5

n = input("Input jumlah: ")
x = int(n)-1
arr = [x]

i=0
while(i <= x):
    arr[i] = input("Input angka array: ")
    arr[i] = int(arr[i])
    i+=1

arr2 = arr.sort()
print(arr2)