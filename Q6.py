import json
file='data.txt'
dict={}
with open(file) as json_data:
    for line in json_data:
        command,discription=line.strip().split(None,1)
        dict[command]=discription.strip()
out_file= open("text.json","w")
json.dump(dict,out_file,indent=4)
out_file.close()