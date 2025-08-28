#Write a program to find the second largest element in the list.
li=[12,34,56,78,9,90]
max=li[0]
smax=0
for i in range(1,len(li)):
    if(li[i]>max):
        smax=max
        max=li[i]
    elif(li[i]>smax):
        smax=li[i]
print("The Maximum element in the list is ",max)   
print("The Second Maximum element in the list is ",smax)          