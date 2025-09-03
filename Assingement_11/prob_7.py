#7. Python Program to Find the Intersection of Two Lists
# same element in two lists
li=[1,2,3,4,5]
li1=[1,2,6,7,8]
inter=[]
for i in li:
    if i in li1 and i not in inter:
        inter.append(i)
print(inter)        

