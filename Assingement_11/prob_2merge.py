#2. Python Program to Merge Two Lists and Sort it
li=[12,34,23]
li1=[56,78,56]
li2=li+li1
for i in range(len(li2)):# here 1 question for i in li2 why not use
    for j in range(len(li2)-i-1):
        if(li2[j]>li2[j+1]):
            li2[j], li2[j+1] = li2[j+1],li2[j]
print(li2)            





# The difference for i in li and for i in range(len[i])
# li2 = [12, 34, 23]

# for i in li2:   # elements
#     print("Element:", i) ## Here we can access only not the index element 

# for i in range(len(li2)):   # Here we can access element as well as index
#     print("Index:", i, "Element:", li2[i])
