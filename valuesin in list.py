a=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
b=[]
for i in a:
    for j in i:
        if type(i[j])==int:
            b.append(i[j])
print(b)