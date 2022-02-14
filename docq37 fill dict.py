a={}
b=[]
c=[]
d=[]
# i=11
for i in range(11,40):
    if i<=19:
        b.append(i)
        a.update({"x":b})
    if i>20 and i<=29:
        c.append(i)
        a.update({"y":c})
    if i>30 and i<=39:
        d.append(i)
        a.update({"z":d})
print(a)

for i in a:
    for j in a[i]:
        if j%5==0:
            print(j)
