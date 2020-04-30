list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

a_dict = {
    "isi": {
        list1[0] : list2[0],
        list1[1] : list2[1],
        list1[2] : list2[2]
    }
    
}

jawaban = list(a_dict.values())[0]
# jawaban = list(a_dict.values())

print(len(jawaban))

# print(jawaban[0])
print(jawaban)
# print(jawaban)
# print(type(a_dict.values()))
