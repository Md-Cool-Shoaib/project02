# import json
# data = '{"Name": "Shoaib","Code": 424,"age": 24,"home": "andaman"}'
# prased= json.loads(data)
# print(prased["Name"])
# data2= {
#     "Name":"P",
#     "dob": 30,
#     "job": False
# }


# if "dob" in data2:
#     del data2["dob"]
# new_data = json.dumps(data2, indent=2)
# print(new_data)
# with open("no.txt", "r") as f:
#     content= f.read(100)
#     print(content,end= "*")

# with open("no.txt", "r") as rf:
#     with open("test.py", 'w') as wf:
#         for lin in rf:
#             wf.write(lin)
# with open("me.jpg", "rb") as rf:
#     with open("copy.jpg", "wb") as wf:
#         for line in rf:
#             wf.write(line)
# x = "jhon"
# def myfunc():
#     global x
#     x = "hennry"
# myfunc()
# print("HE is"+x)
# fruits = ["banana", "apple", "mango", "cherry"]

# newlist = [x for x in fruits if "a" in x]
# print(newlist,end=" ")
is_even = [x for x in range(1,10) if x % 2 == 0]
print(is_even)