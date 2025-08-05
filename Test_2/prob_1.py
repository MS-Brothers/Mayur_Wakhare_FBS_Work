# Leap Year
y = int(input('Enter the year : '))
if(y % 4 == 0)and((y%400==0)or (y%100 !=0)):
    print(f'{y} is a leap year')
    
else:
    print(f'It is not a leap year')

