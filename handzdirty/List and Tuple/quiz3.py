list1 = [5, 20, 15, 20, 25, 50, 20]

# x = 0
# for x in list1: 
#     if list1[x] == 20:
#         remove(list1[x])

i = 0
while(i<=6):
    if list1[i] == 20:
        list1[i].remove()
    i+=1
# favoriteCar.append(favoriteMot)

print(list1)
