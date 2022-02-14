my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
l=[]
i=0
max=0
for i in my_dict:
    if max<my_dict[i]:
        max=my_dict[i]
        s=i
print(s)
max1=0
for i in my_dict:
    if max1<my_dict[i]:
        if max!=my_dict[i]:
            max1=my_dict[i]
            j=i
print(j)
max2=0
for i in my_dict:
    if max2<my_dict[i]:
        if max!=my_dict[i]:
            if max1!=my_dict[i]:
                max2=my_dict[i]
                k=i
print(k)
l.append(s)
l.append(j)
l.append(k)
print(l)