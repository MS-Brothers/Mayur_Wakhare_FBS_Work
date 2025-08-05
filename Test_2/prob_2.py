#Write a program to accept 3 digit number. If first digit is double of second digit and half of third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
digit = int(input('Enter the 3 digit number :'))
num_1=digit
d1= num_1 // 100
num_1 = num_1 % 100
d2= num_1 // 10
num_1= num_1 % 10

if(d1 == d2*2 and d1 == num_1 /2):
    print(f'Yes , You have done it')
else:
    print(f'Please try next time')    


