list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
# di=dict(zip(list1,list2))
# print(di)
i=0
dict={}
while i<len(list1):
    dict[list1[i]]=list2[i]
    i=i+1
print(dict) 
