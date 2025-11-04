#Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!

def fatc(a):
    temp=a
    fact=1
    sum=0
    for i in range(1,a+1):
        fact*=i
        sum+=fact
    return sum
n=int(input('Enter the number : '))
res=fatc(n)
print(res)    


# #Write a program to print fibonacci series
# def recc(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return recc(n-1)+recc(n-2)
# n=int(input('Enter the number:'))
# res=recc(n)
# print(res)    
        