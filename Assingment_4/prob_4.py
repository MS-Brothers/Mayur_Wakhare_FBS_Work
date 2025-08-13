#WAP to print the factorial of number 
n=int(input('Enter the number : '))
fact =1
for i in range(n,0,-1):#Using range different 
    # start =n , stop =0(Exclusive the loop stop before it reaches 0)
    # -1 is for GO Backwards
    fact *=i
print(f'The factorial of {n} is {fact}')


#Using normal range 1 to n

n=int(input('Enter the number : '))
fact=1
for i in range(1,n+1):
    fact *= i
print(f'The factorial of {n} is {fact} ')    



# Another Method
n=int(input('Enter the number : '))
temp =1
i=1
while(i<=n):
    temp *= i
    i+=1
print(f'The factorial of {n} is {temp}')    