#Write a program to create a new list from existing list which contains cube of each number of list.
li=[12,34,1,2,3,4,5]
lis=[]
for i in li:
    lis.append(i**3)
   # lis.append(li[i]**3)#i itself is the element of the list, not the index. So li[i] is wrong (because you’re treating i as an index).
print(lis)    