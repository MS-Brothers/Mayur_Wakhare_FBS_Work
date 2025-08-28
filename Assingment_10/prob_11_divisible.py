#Write a program to print all numbers which are divisible by m and n in the list.
m=int(input('Enter the number : '))
n=int(input('Enter the number : '))
li=[12,23,45,21,67,88,78,12]
div=[]
for i in li:
    if(i%m==0 and i%n==0):
        div.append(i)
print(div)        