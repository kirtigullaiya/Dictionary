a={"c1":"red","c2":"green","c3":None}
b={}
for i in a:
    if a[i]==None:
        pass
    else:
        b.update({i:a[i]})
print(b)