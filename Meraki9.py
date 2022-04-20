
import json
a={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
b=input("Enter the items you want to purchase:- ")
c=int(input("Enter the number of items:- "))
for i in a:
    if a[i][b]==a[i][b]:
        d=a[i][b]
        e=int(d)
        print("The remaining number of items are ",e-c)
        f={}
        dic={}
        n=e-c
    for key in a:
        for value in a[key]:
            f[value]=a[key][value]
            if value==b:
                f[value]=n
                dic[key]=f

with open ("Meraki9.json","w") as f:
    json.dump(dic,f,indent=4)














