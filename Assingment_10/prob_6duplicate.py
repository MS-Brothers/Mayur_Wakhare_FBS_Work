#6. Write a program to remove duplicates from the list.
li=[45,67,8,8,954,445,56]
lis=[]
for i in li:
    if i not in lis:
        lis.append(i)
print(lis)        