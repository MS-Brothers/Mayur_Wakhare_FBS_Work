#Write a program to check if given number is Armstrong number or not.(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)
n=int(input('Enter the number : '))
order=len(str(n))
temp=n
sum=0

while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if(n==sum):
    print(f'{n} is a Armstrong Number')
else:
    print(f'{n} is not a Armstrong Number')        