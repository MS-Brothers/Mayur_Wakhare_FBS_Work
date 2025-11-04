# Write a program to find sum of digits using recursion.
def sum(n):
    if n==0:
        return 0
    else:
        d=n%10
        return d+sum(n//10)
    
n=int(input('Enter the number:'))    
res=sum(n)
print(res)