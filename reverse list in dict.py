# output-{"A"[7,0,9,3],"B":[5,4,2,6]}
a={"A":[3,9,0,7],"B":[6,2,4,5]}
b=[]
c=[]
d={}
for i in a:
    if i=="A":
        j=1
        while j<len(a[i])+1:
            b.append(a[i][-j])
            j+=1
        d.update({i:b})
    elif i=="B":
        j=1
        while j<len(a[i])+1:
            c.append(a[i][-j])
            j+=1
        d.update({i:c})
print(d)