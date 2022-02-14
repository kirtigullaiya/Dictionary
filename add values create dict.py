a=[2,4,5,7]
b={}
add=0
j=0
for i in a:
    add+=i
    b.update({j:add})
    j+=1
print(b)
