a={0:10,1:20}
b={}
key=int(input("please enter key:"))
value=int(input("please enter value:"))
i=1
while i<=key:
    a.update({i:value+10})
    i+=1
    value+=10
print(a)
