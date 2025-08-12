#Write a program to swap two numbers using third variable.
a=int(input('Enter the first number : '))
b=int(input('Enter the second  number : '))

temp =a
a=b
b=temp
print(f'The first number is {a}, and Second number is {b}')