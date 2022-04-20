
list=["2345"]
i=0
while True:
    a=list[0][i]
    b=int(a)
    print(b*b,end="")
    if list[0][i]==list[0][-1]:
        break
    i=i+1
    