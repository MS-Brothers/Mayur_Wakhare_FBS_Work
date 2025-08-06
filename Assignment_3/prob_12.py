#Write a program to check if given 3 digit number is a palindrome or not.
num_1=int(input('Enter the number : '))
d1 = num_1 % 10
d2 = num_1 // 10
d2 = d2 %10
d3 = num_1 // 100
print(f'{d1}{d2}{d3}')
#check palindrome 
num_2 = (d1*100)+(d2*10)+d3
print(f'{num_2}')
if(num_1==num_2):
    print(f'It is Palindrome')
else:
    print(f'It is not a Palindrome')    