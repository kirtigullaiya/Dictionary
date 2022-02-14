a=[{"v":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
d=[]
for i in a:
    for j in i.values():
        if j not in d:
            d.append(j)
d=set(d)
print(d)
