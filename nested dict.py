a=[1,2,3,4]
b={}
c={}
b=c
for i in a:
    c[i]={}
    c=c[i]
print(b)