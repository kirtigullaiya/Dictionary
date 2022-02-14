a="MISSISSIPPI"
count={}
for x in a:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1
print(count)

str=input("enter the string")
print("string  is",str)
count={}
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1
print(count)            


