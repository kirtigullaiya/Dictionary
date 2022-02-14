a=[1,2,3,4,5]
b=["name","age","class","roll-no"]
c=[["aarav",14,"9th",32],["amit",12,"7th",7],["saniya",12,"7th",34],["kiran",10,"5th",23],["prince",14,"8th",15]]
d={}
for i in a:
    for j in b:
        for k in c:
            for l in k:
                d.update({i:{j:{l}}})
print(d)

