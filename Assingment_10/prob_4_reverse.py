#Write a program to reverse the list.
li=[10,3,4,5,6]
rev = []
for i in range(len(li)-1, -1, -1): 
    rev.append(li[i])

print("Original list:", li)
print("Reversed list:", rev)
