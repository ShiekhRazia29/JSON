#convert python dictionary sort by keys in json object
import json
data={'5':'Razia',
'4':'Sheetal',
'1':'Sabrina',
'3':'Aabiru',
'2':'Jabeena'}
sorted_keys={k:v for k,v in sorted(data.items())} # used to sort the dictionary according to its keys
print(sorted_keys)
data2=json.dumps(sorted_keys) #dump the sorted to convert in json object
print(data2) 