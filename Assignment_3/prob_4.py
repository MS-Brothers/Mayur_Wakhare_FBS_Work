#Write a program to input all sides of a triangle and check whether triangle is valid or not.
a=int(input('Enter the first side :'))
b=int(input('Enter the second side :'))
c=int(input('Enter the third side :'))

if(a>b+c and b>a+c and c>a+b):
    print(f'It is valid triangle ')
else:
    print(f'It is not a valid triangle')    
