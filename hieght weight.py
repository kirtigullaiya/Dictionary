a={"cierra":(6.2,70),"aiden cantrell":(5.9,65),"kierra gentry":(6.0,68),"pierre cox":(5.8,66)}
height=float(input("please enter height:"))
weight=int(input("please enter weight:"))
for i in a:
    for j in a[i]:
        # for k in a[i]:
        if j>height and j>weight:
            print(i,":",a[i])