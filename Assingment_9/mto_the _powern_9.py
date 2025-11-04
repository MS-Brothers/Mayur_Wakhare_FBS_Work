# Write a program to calculate the m to the power n using recursion.
def power(m,n):
    if n==0:
        return 1
    else:
        return m*power(m,n-1)
m=int(input('Enter the m number:'))
n=int(input('Enter the n number:')) 
res=power(m,n)
print(res)   
    