# remove key from dictionary.
a={"a":10,"b":20,"c":30}
b={}
key=input("please enter key:")
for i in a:
    if i==key:
        pass
    else:
        b.update({i:a[i]})
print(b)

