#9. Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.
li=[11,34,56,78,90,45,67,89,23]
count=0
even=[]
odd=[]
for i in li:
    count+=1
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)   
print("Even element List :",even)
print("Odd element list : ",odd) 
print(count," elements in the list")        

    
