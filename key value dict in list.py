# question64 of w3 resource.
a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
c={}
b=[]
for i in a:
    for j in a[i]:
        c.update({i:j})

b.append(c)

print(b)