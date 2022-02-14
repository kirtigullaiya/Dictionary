d={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
dict={}
for i in d.values():
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)