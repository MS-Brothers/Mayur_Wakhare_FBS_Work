#Write a program to print list after removing even numbers.
li=[34,56,78,90,21,32,23,45,67,89]
new=[]
for i in li:
    if(i%2!=0):
        new.append(i)
print(new)        