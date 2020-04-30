buka_paragraf = open("sumber.txt", "r")
buka_tujuan = open("hasil.txt", "w")

paragraf = buka_paragraf.read()
buka_paragraf.close()

buka_tujuan.write(paragraf)

# hasil = buka_tujuan.read()

# print(hasil)