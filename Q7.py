import json
list1=["Neelam","Programmer","24","2400"]
key1=["name","Designation","Age","salary"]
emp1={}
for keys in key1:
    for values in list1:
        emp1[keys]=values
        list1.remove(values)
        break
#print(str(emp1))
list1=["komal","Trainer","24","20000"]
key1=["name","Designation","Age","salary"]
emp2={}
for keys in key1:
    for values in list1:
        emp2[keys]=values
        list1.remove(values)
        break
#print(str(emp2))
list1=["Anirudh","HR","26","22000"]
key1=["name","Designation","Age","salary"]
emp3={}
for keys in key1:
    for values in list1:
        emp3[keys]=values
        list1.remove(values)
        break
#print(str(emp3)) 
list1=["komal","Trainer","24","20000"]
key1=["name","Designation","Age","salary"]
emp4={}
for keys in key1:
    for values in list1:
        emp4[keys]=values
        list1.remove(values)
        break
#print(str(emp4))
dict1={}
dict1.update({"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4})
print(dict1)
with open("Q7.json","w") as json_file:
 json.dump(dict1,json_file,indent=3)

