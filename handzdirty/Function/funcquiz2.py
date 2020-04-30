batas = 50

# def pembatas(batas):
#     arr = []
#     i = 0
#     while (i<batas):
#         arr.append(i)
#         i+=1
#     return arr

# pembatas = lambda x: list(range(x))

def tambah(batas):
    n_list = list(range(batas))
    m = 0
    jawaban = 0

    while(m<50):
        jawaban = jawaban + n_list[m]
        m+=1
    
    return jawaban

    # for i in batas:
    #     jawaban = batas[m]
    #     m+=1
    # return jawaban


# def sum_list(n):
#     n_list = list(range(n))

#     total = 0

#     for i in n_list:
#         total += i
#     return total


b = tambah(batas)
print(b)