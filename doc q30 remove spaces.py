a={'s  001':["maths","science"],"s   002":["maths","english"]}
b={}
for i in a:
    for j in i:
        k=i.replace(" ","")
        for i,x in a.items():
            b.update({k:x})
print(b)
            

