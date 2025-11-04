# Write a program to find sum of n numbers using recursion.
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
n=int(input('Enter the number:'))    
res=sum(n)
print(res)