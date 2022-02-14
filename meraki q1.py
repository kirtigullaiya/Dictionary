dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for i in dic1:
    for j in dic2:
        for k in dic3:
            if i==j:
                add=dic1[i]+dic2[j]
                dic4.update({i:add})
            elif j==k:
                add=dic2[j]+dic3[k]
                dic4.update({j:add})
            else:
                dic4.update({i:dic1[i]})
                dic4.update({j:dic2[j]})
                dic4.update({k:dic3[k]})
print(dic4)


    