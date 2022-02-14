a=[{"item":"item1","amount":400},{"item":"item2","amount":300},{"item":"item1","amount":750}]
b={}
for i in a:
    if i["item"] in b.keys():
        b[i["item"]]+=i["amount"]
    else:
        b[i["item"]]=i["amount"]
print(b)            


