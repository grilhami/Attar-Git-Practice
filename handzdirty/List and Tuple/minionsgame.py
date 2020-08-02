kata = input() #BANANA
kata.split() #'b' 'a' 'n' 'a' 'n' 'a'

skor_stuart = 0
skor_kevin = 0
kosong1 = []
kosong2 = []
for i in kata:
    if(i == 'q'|'w'|'r'|'t'|'y'|'p'|'s'|'d'|'f'|'g'|'h'|'j'|'k'|'l'|'z'|'x'|'c'|'v'|'b'|'n'|'m'):
        for j in kata[1:]:
            kosong1.append(j)
            if(j == kosong1): #a == ba, 
                skor_stuart+=1