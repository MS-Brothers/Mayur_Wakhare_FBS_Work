#Sum of all odd numbers between 1 to n
def odd(a):
    sum=0
    for i in range(1,a+1):
        if(i%2!=0):
            sum+=i
        
    return sum    
b=int(input('Enter the number : '))
res=odd(b)
print(f'{res}') 


