list1 = [1, 2, 3]
list2 = [3, 4, 5]
iter=0

for i in list1:
    if(i == list2[iter]):
        break
    else:
        print(i, " not in list2")

for j in list2:
    if(j == list1[iter]):
        break
    else:
        print(j, " not in list2")
        
        

# for i in list1:
#     for j in list2:
#         if(j != i):
#             # print(j, i)
#             # print(j, " not in list2" )
#     print(j, " not in list2" )    
            



