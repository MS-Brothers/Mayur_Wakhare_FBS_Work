#Write a program to find print the following Fibonacci series using functions: 1 1 2 3 5 8 n terms
def fibo(f):
    a=1
    b=0
    sum=0
    for i in range(1,f+1):
        c=a+b
        sum+=c
        a=b
        b=c
    return sum    
f=int(input('Enter the number : '))        
res=fibo(f)
print(f'The sum of Fibonacii series is {res}')