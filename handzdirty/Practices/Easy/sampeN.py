n = input()
n = int(n)
i = 1
a_list = []
jawab = ''

while(i <= n):
    a_list.append(i)
    i+=1

x=0
for y in a_list:
    y = str(y)
    a_list[x] = y
    x+=1

for j in a_list:
    jawab = jawab + j

print(jawab)