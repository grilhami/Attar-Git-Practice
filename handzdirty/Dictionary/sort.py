shop_items = [
    {"amount": 3.500},
    {"amount": 2.500},
    {"amount": 3.000},
    {"amount": 15.000},
    {"amount": 13.431}
]
temp = 0

# {"indomie": 3.500,
#     "sabun": 2.500,
#     "aqua": 3.000,
#     "kecap": 15.000,
#     "sambal": 13.431
# }

for i in shop_items:
    for j in shop_items[1:]:
        if(i["amount"] < j["amount"]):
            temp = i["amount"]
            i["amount"] = j["amount"]
            j["amount"] = temp

print(shop_items)


