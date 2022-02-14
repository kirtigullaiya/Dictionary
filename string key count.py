# question48 of doc
a={1:"red",2:"green",3:"black",4:"white",5:"black"}
b={}
for i in a:
    length=len(a[i])
    b.update({a[i]:length})
print(b)