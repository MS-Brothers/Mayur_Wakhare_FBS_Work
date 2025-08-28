#Write a program to find maximum and minimum element in a list.
li = [10, 20, 30, 40, 50,5]   
max = li[0]                 

for i in range(1, len(li)): 
    if li[i] >max:         
        max = li[i]       

print("Maximum number is", max)


li = [10, 20, 30, 40, 50,5]   
min = li[0]                 

for i in range(1, len(li)): 
    if li[i] < min:         
        min = li[i]       

print("Maximum number is", min)
