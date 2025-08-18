#Write a program to check if entered year is a leap year or not.
def leaf(a):
    temp=a
    while temp>0:
        if(temp%4==0 or(temp%400==0 and temp%100!=0)):
            return True
        else:
            return False
n=int(input('Enter the year : '))
res=leaf(n) 
if(res):
    print(f'This is a leaf Year')
else:
    print(f'This is not a leaf year')           