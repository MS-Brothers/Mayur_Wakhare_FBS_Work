#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gen=(input('Enter your gender : '))
age=int(input('Enter your age : '))

if(gen == 'male' and age >=21) or (gen=='female' and age >=18):
    print(f'You are eligible')
else:
    print(f'You are not eligible')    
