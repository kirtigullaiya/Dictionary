a={'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
b={}
for i in a:
    for j in a[i]:
        b.update({i:a[i][j]})
print(b)