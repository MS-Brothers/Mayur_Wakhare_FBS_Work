#WAP to calculate area of rectangle and triangle
a=int(input('Enter 1 for Area of Rectangle,\n Enter 2 for Area of Triangle :  '))

if(a==1):
    len =float(input('Enter the Lenght of Rectangle : '))
    bre =float(input('Enter the Breadth of Rectangle : '))
    area = len * bre
    print(f'The Area of Rectangle is {area}')
elif(a==2):
    high=float(input('Enter the Height of Triangle : '))
    base=float(input('Enter the base of triangle : '))
    area = 1/2 * high*base
    print(f'The Area of triangle is {area}')
else:
    print(f'Invalid Input ')        




