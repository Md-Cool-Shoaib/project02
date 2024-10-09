import json

data = '{"Var1": "harry", "Var2": 56}'


prased = json.loads(data)
print(prased['Var1'])


data2 = {
    "Name": "Md Shoaib",
    "cars": ["Suv","Mountain Car", "Water car"],
    "fridge": ("No",99),
    "isFridge": False
}
jscomp = json.dumps(data2, sort_keys = True)
print(jscomp)