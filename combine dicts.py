# output-{'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}
a={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
b={'x': 300, 'y': 'Red', 'z': 600}
c={}
for i in a:
    for j in b:
        if i in b:
            c.update({i:[a[i],b[i]]})
        else:
            c.update({i:[a[i]]})
print(c)
