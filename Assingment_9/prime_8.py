# Write a program to check whether a number is prime or not using recursion.
def prime(n,i=2):
    if n==0:
        return f'0 is not a prime  number'
    elif n==1:
        return f'1 is not prime nor composite'
    if i*i>n:
        print(f'{n} is a Prime number.')
    elif n%i==0:
        print(f'{n} is not a prime number.')    
    else:
        return prime(n,i+1) 
    
n=int(input('Enter the number:'))
res=prime(n)       