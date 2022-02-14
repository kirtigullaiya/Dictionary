# square.
d={}
i=1
num=int(input("please enter number:"))
while i<=num:
    square=i**2
    d.update({i:square})
    i+=1
print(d)