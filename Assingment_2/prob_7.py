# The sum of three digit number
num1=int(input('Enter the three digit number : '))
d1=num1 % 10 # 123 = 3
temp = num1 // 10 # 123 = 12
d2 = temp % 10 # 12 = 2
temp = temp // 10 # 12 = 1
print(f'The sum of three digit number is {num1} = {d1+d2+temp}')
