#Write a program to find sum of digits of a number.
def series(sum):
   temp=sum
   total=0
   for i in range(1,sum+1):
      a=temp%10
      temp//=10
      total+=a
   return total  
n=int(input('Enter the number : '))
res=series(n)
print(f'The sum is {res}')
    