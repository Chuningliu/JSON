import json
a=["neelam","Programmer","24","2400",]
b=["Komal","Trainer","24","20000"]
c=["Anuradha","HR","25","40000"]
d=["Abhishek","Manager","29","63000"]
e=["Name","Designation","Age","Salary"]
emp1={}
emp2={}
emp3={}
emp4={}
j={}
k=["emp1","emp2","emp3","emp4"]
i=0
while i<len(e):
    aa=[]
    emp1[e[i]]=a[i]
    emp2[e[i]]=b[i]
    emp3[e[i]]=c[i]
    emp4[e[i]]=d[i]
    aa.append(emp1)
    aa.append(emp2)
    aa.append(emp3)
    aa.append(emp4)
    i+=1
i=0
while i<len(k):
    j[k[i]]=aa[i]
    i+=1
print(j)


with open ("Meraki8.json","w") as f:
    json.dump(j,f,indent=4)

