import json
with open ("Q1.json","r")as read_file:
    data=json.load(read_file)
print(type(data))
print(data)
