#WAP to print sum of series upto n
n=int(input('Enter the Number : '))
for i in range(1,n+1):
    s=i*(i+1)//2
    print(f'{s}')