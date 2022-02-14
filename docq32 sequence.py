# a={1:10,2:20,3:30,4:40,5:50}
# print("key","value","count",end="")
# print()
# count=0
# for i in a:
#     count+=1
#     print(i," ",a[i],"  ",count)

a={"c1":[1,2,3],"c2":[5,6,7],"c3":[9,10,11]}
for i in a:
    print(i,end="  ")
print()
for i in a:
    for j in a[i]:
        if j==1 or j==5 or j==9:
            print(j,end="   ")
