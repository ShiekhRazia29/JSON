import json
# import json
#convert python nobject to json string
dict={'Name':'Razia','course':'Engineering','place':'beerwah'}
print(type(dict))
dict1=json.dumps(dict)
print(type(dict1))
print(dict1)
# with open("Q2.json","w") as json_string:
#     json.dumps(dict,json_string)
