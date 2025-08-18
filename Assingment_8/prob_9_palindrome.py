#Write a program to check if entered number is a palindrome or not.
def pali(a):
    temp=a
    rev=0
    while temp>0:
        d=temp%10
        rev=rev*10+d
        temp//=10
    if(a==rev):
        return True
    else:
        return False
n=int(input('Enter the number : '))
res=pali(n)
if(res):
    print(f'The number is Palindrome') 
else:
    print(f'The number is not a palindrome')           
