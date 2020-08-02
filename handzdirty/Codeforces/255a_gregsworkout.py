a = int(input()) #7
b = input()
b = b.split()
b = b[:a] # 5 1 10 1 4 12 3

total = [0, 0, 0]

x = 0
for i in b:
    i = int(i)
    b[x] = i
    x+=1

#9 5 22
q = 0
for j in range(len(b)):
    if(q < len(b)):
        total[0] = total[0] + b[q]
        q += 3
    else:
        break
w = 1
for j in range(len(b)):
    if(w < len(b)):
        total[1] = total[1] + b[w]
        w += 3
    else:
        break    

e = 2
for j in range(len(b)):
    if(e < len(b)):
        total[2] = total[2] + b[e]
        e += 3  
    else:
        break  

# print(total)
if(total[0] == max(total)):
    print("chest")
elif(total[1] == max(total)):
    print("biceps")
elif(total[2] == max(total)):
    print("back")
