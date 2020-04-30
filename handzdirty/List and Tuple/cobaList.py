favoriteCar=["Spyker", "Lincoln", "Buick"]
favoriteMot=["Ducati", "BMW", "Harley"]
print(favoriteCar[1])
favoriteCar[2] = "Aston Martin"
print (favoriteCar[2])

# favoriteCar.append("Mclaren", "Ferarri", "Mercedes")
favoriteCar.append("Mclaren")
print(favoriteCar)

favoriteCar.insert(1, "Ferarri")
print(favoriteCar)

# print(favoriteCar.sort())

favoriteCar.sort()
print(favoriteCar)

favoriteCar.append(favoriteMot)
print(favoriteCar)

favoriteCar.extend(favoriteMot)
print(favoriteCar)
x=0
for x in favoriteCar:
    print(favoriteCar.index(x))


