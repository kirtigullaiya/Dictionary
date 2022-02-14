d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
# d3={}
for i in d1:
    # for j in d2:
        if i in d2:
            # add=d1[i]+d2[j]
            # d3.update({i:add})
            d2[i]=d2[i]+d1[i]
        else:
            d2[i]=d1[i]
print(d2)
# for i in d1:
#     for j in d2:
#         if d1[i]==d2[j]:
#             add=d1[i]+d2[j]
#             d3.update({i:add})
# print(d3)


# a=1056000