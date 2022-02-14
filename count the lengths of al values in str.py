a={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
add=0
for i in a:
    length=len(a[i])
    add+=length
print(add)