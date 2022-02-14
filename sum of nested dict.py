a={1:{"course":"python","fees":20000},2:{"course":"javascript","fees":15000}}
sum=0
for i in a:
    for j in a[i]:
        if type (a[i][j])==int:
            sum+=a[i][j]
print(sum)            

