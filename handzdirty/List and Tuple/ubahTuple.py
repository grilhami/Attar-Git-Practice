tuple1 = (11, [22, 33], 44, 55)
temp = list(tuple1)

a = temp[1]
a[0] = 222
temp[1] = a

tuple1 = tuple(temp)
print(tuple1)