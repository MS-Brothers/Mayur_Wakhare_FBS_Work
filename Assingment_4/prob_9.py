#WAP to print all numbers in a range divisible by a given number.
n=int(input('Enter the number : '))
r=int(input('Enter the range : '))

for i in range(1,r):
    if(i%n==0):
        print(f'{i}')
else:
    pass        