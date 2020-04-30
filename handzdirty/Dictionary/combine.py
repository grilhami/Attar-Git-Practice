dicts = [
    { "item": "item1", "amount": 400 },
    { "item": "item2", "amount": 300 },
    { "item": "item1", "amount": 750 }
]
iter=1

jawaban = [
    {"amount": 0}, 
    {"amount": 300}
]

for i in dicts:
    if (i["item"] in dicts[iter]["item"]):
        jawaban[0]["amount"] = i["amount"] + dicts[iter]["amount"]

    iter+=1



    # else:
    #     jawaban[1]["amount"] = i["amount"] + dicts[iter]["amount"]

    # if(i["item"] == dicts[iter]["item"]):
    #     jawaban[0]["amount"] = i["amount"] + dicts[iter]["amount"]
    # iter+=1    


# jawaban[0]["amount"] = dicts[0]["amount"] + dicts[2]["amount"]
# jawaban[1]["amount"] = dicts[1]["amount"]

print(jawaban)