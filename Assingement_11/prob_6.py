#6. Python Program to Find the Union of two Lists
li=[12,45,4,44,7,55]
li1=[34,54,44,55,9]

li2=li.copy()
for i in li1:
    if i not in li2:
        li2.append(i)
print(li2)        