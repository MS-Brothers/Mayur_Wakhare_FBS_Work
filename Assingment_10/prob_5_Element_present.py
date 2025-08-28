#Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.
a=int(input('Enter the number : '))
li=[12,45,6,78,9,90,45]
count=0
for i in range(len(li)):
    if(li[i]==a):
        count+=1
if(count>0):
    print(f'{a} is present in the list and count is {count}.')
else:
    print(f'{a} is not present in the list.')    


