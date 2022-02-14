a={"cierra vega":175,"aiden cantrell":180,"kierra gentry":165,"pierre cox":190}
num=int(input("please enter number:"))
b={}
for i in a:
    if a[i]>num:
        b.update({i:a[i]})
print(b)
