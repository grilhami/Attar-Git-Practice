buka = open("teks.txt", "r")
kata = buka.read()
buka.close()

# print("Nama file: ", buka.name)
itung = kata.split()
print("\"",kata,"\"", "has", len(itung), "words")
