# Sample Input
# 5

# Sample Output
# 0
# 1
# 4
# 9
# 16

n = input("Input: ")
x = int(n) - 1
i=0; tambah=1; jawab=0

print(i)
while(i < x):
    jawab+=tambah
    print(jawab)
    tambah+=2
    i+=1