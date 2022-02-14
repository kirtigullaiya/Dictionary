a=[("yellow",1),("blue",2),("yellow",3),("blue",4),("red",1)]
b={}
c=[]
for i in a:
    for j in i:
        if type(j)==str:
            for k in i:        
                if type(k)==int:
                        # c.append(k)
                    b.update({j:[k]})
print(b)