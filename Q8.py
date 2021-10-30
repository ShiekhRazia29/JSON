import json


dict={
    "shopping_list":
    {
        'choco':'15',
        'Biscuits':'50',
        'Dairy_milk':'30',
        'ice_cream':'20'
    }
}
items=input("Enter the name of the item:")
for item in dict.values():
    quantity=int(input("Enter the quantity:"))
    print(int(items) - quantity)
with open("Q8.json","w") as shop_list:
    json.dump(dict,shop_list,indent=4)



