#Write a program to check whether the triangle is equilateral, isosceles or scalene

a=int(input('Enter the first side : '))
b=int(input('Enter the second side : '))
c=int(input('Enter the third side : '))

if(a==b==c):
    print(f'It is equilateral triangle')
elif(a==b or b==c or a==c):
    print(f'It is a isosceles triangle')
else:
    print(f'It is scalene triangle')        
