import json
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/posts") as response:
    source = response.read()
    print(source)

data = json.loads(source)
# print(json.dumps(data, indent= 2))

# print(len(data['dict']['userId']))


for item in data[:50]:
    user_id = item.get('userId')
    name = item.get('body')  # Get the userId
    
    # Print the remaining information
    print(f"UserId: {user_id} Name: {name}")
print(f"Total number of Information Gathered: {len(data)}")

# print('after deletion')
# print(json.dumps(data, indent= 2))