# 10. Write a program to reverse a number using recursion.
def reve(n,rev=0):
    if n==0:
        return rev
    else:
        d=n%10
        rev=rev*10+d
        return reve(n//10,rev)
n=int(input('Enter the number:'))    
res=reve(n)
print(res)