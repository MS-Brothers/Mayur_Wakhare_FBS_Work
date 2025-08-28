#Write a program to remove all occurrences of a given element in the list.
li=[12,34,45,67,67,78,67,90,67]
a=int(input('Enter the number : '))
new=[]
for i in li:
    if(i !=a):
        new.append(i)
print(new)        
