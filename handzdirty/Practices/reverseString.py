isi = input()  #blue-green-yellow
balik = lambda isi : isi.split("-")
# isi = isi.split("-") # ['blue', 'green', 'yellow']
# isi.reverse()

jawab = balik(isi)
jawab.reverse()


def ini_function(masuk):
    hasil=''
    for i in masuk:
        if(i != masuk[-1]):
            hasil += i + '-'
        
        else:
            hasil += i
    return hasil

result = ini_function(jawab)
print(result)