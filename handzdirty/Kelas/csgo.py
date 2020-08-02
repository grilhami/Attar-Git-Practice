from Weaponry import Weapons
from AWP import Awp



nama_senjata = []
damage_senjata = []
rof_senjata = []

for index in range(2):
    input_nama = input("Input nama senjata: ")
    input_damage = input("Input nama damage: ")
    input_rof = input("Input nama rof: ")

    nama_senjata.append(input_nama)
    damage_senjata.append(input_damage)
    rof_senjata.append(input_rof)
    name = nama_senjata[index]
    damage = damage_senjata[index]
    rof = rof_senjata[index]

    senjata = Weapons(name, damage, rof)
    print(senjata.name)
    print(senjata.damage)



























# ak47 = Weapons()
# ak47.name = "AK-47"
# ak47.damage = 33
# ak47.rof = 4 
# ak47.scoping(has_scope = True)

# uzi = Weapons
# uzi.name = "Uzi"
# uzi.damage = 17
# uzi.rof = 7 

# print(ak47.scoping())

# awp = Awp()
# print(awp.name)
# print(awp.damage)
# print(awp.rof)
# print(awp.scoping(has_scope = True))
