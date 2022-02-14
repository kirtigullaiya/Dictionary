# d1={"a":100,"b":200,"c":300}
# d2={"a":300,"b":200,"c":100}
# # sum=0
# for i in d1:
#     # for j in d2:
#     sum=d1[i]+d2[i]
#     print(sum)

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)