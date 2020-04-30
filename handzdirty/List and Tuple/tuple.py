a = input("Input tuple: ")




# while(i<2):
#     campur(i) =  input("Input:")


# a = input("Input 1: ")
# b = input("Input 2: ")
# c = input("Input 3: ")

# merk = (100, 200, 300)
# var1 = merk[0]
# var2 = merk[1]
# var3 = merk[2]
# z
# print(var1)
# print(var2)
# print(var3)
if("(" not in a or ")" not in a):
    print("Must use ()")

else:
    hasil = a.replace("(", "").replace(")", "")

    print("This is a tuple: {}".format(a))