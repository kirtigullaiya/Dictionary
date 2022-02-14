a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
for i in a:
    for j in i:
        num=int(i[j])
        a.append({j:num})
print(a)