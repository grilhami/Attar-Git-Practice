numbers = [2, 32, 4, 64, 52, 10]

j=0
current = numbers[j]

for i in numbers:
    if(current < i):
        current = i


print(current)