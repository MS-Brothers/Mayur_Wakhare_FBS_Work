#WAP Union of two lists without using set concept
li=[1,2,3,4,5,6,6]
li1=[5,6,7,8,9]
li3=[]
for i in li+li1:
    if i not in li3:
        li3.append(i)
        
print(li3)            