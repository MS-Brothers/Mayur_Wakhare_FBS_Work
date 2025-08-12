#WAP to check if a given number is prime number or not.
n=int(input('Enter the number : '))
for i in range(1,n//2+1):
    if(n%2==0):
        print(f'{n} it is not a prime number ')
        break
else:
    print(f'{n} It is a prime number ')        