#convert python object to json data
import json
string={'plcaes':['beerwa','Srinagar','ratnagiri']}
#jsondata=json.dumps(string)
#print(jsondata)
with open("Q3.json","w") as JSON_data:
    json.dump(string,JSON_data)
