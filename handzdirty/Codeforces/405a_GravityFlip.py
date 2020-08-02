a = input()
a = int(a)
b = input()
b = b.split()
b = b[:a]

x=0
for i in b:
    i = int(i)
    b[x] = i
    x+=1

b.sort()

for i in b:
    print(i)