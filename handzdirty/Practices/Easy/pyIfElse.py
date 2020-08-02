n = input()
n = int(n)

if(n>=2 & n<=5):
    if(n%2 == 0):
        print("Not Weird")
    else:
        print("Weird")
    
elif(n>=6 & n<20):
    if(n%2 == 0):
        print("Weird")
    else:
        print("Not Weird")
else:
    if(n%2 == 0):
        print("Not Weird")
    else:
        print("Weird")