import json
with open('states.json', 'r') as f:
    data = json.load(f)
for states in data['states']:
    del states['area_code']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent= 2)
    # print(states['name'], states['capital'])
# people_string = '''
# {
#     "people": [
#         {
#             "name": "Md Shoaib",
#             "phone": "9693267012",
#             "emails": ["mdshoaib@nomail.com", "mdshoaibwork@nomail.com"],
#             "has_licence": false
#         },
#         {
#             "name": "saqib",
#             "phone": "62083123560",
#             "emails": null,
#             "has_licence": true
#         }
#     ]
# }
# '''
# data = json.loads(people_string)
# print(type(data['people']))
# for person in data['people']:
#     del person['phone']
# new_string= json.dumps(data, indent = 2, sort_keys=True)
# print(new_string)