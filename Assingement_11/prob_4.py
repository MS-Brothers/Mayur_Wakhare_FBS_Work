#Python Program to Find the Second Largest Number in a List Using Bubble Sort
li=[12,45,43,65,78,90,65]
smax=li[0]
max=0
for i in range(len(li)):
    for j in range(len(li)-i-1):
        if(li[j]>li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]

print(li)
print(f'The second largest element is : {li[len(li)-2]}')            
                

        