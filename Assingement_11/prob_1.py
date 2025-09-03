#1. Python Program to Put Even and Odd elements of a List into two Different Lists
n=int(input('Enter the number of element in the list : '))
li=[]
for i in range(n):
    val=int(input(f'Enter the element {i+1} : '))
    li.append(val)
print(li)    





#li=[12,43,56,67,88,89,90,67]
even=[]
odd=[]
for i in li:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(f'Even Element : {even}')  
print(f'Odd Element : {odd}')          