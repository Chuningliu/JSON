import json
a=[10,10,20,50,50,30,10,20,20,10]
b=[]
i=0
count=0
while i<len(a):
    j=i+1
    while j< len(a):
        if a[i]==a[j]:
            c=a[i],a[j]
        if c not in b:
            b.append(c)
            count+=1
        j+=1
    i+=1
print("There is ",count,"pairs")

with open("pairs_count.json","w") as f:
    json.dump(count,f)
