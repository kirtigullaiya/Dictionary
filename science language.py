a={"science":[88,89,62,95],"language":[77,78,84,80]}
b=[]
for i in a:
    for j in a[i]:
        print(j)
        b.append({i:j})
print(b)