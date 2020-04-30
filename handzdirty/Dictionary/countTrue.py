dicts = [
    {'id': 1, 'success': True, 'name': 'Lary'}, 
    {'id': 2, 'success': False, 'name': 'Rabi'}, 
    {'id': 3, 'success': True, 'name': 'Alex'}
]

jawaban = 0
for i in dicts:
    if(i["success"] == True):
        jawaban+=1

print(jawaban)


