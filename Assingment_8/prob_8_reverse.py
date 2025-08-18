#Write a program find reverse of a number
def rev(a):
    re=0
    temp=a
    while temp>0:
        s=temp%10
        re=re*10+s
        temp//=10
    return re
n=int(input('Enter the number : '))
res=rev(n)
print(f'The reverse number is : {res}')    