#Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random
user_id = 'mayur_wakhare'
Password = 'xy23a'

a=input('Enter the userID : ')
b=input('Enter the Password : ')
if(user_id==a and Password==b):
    print(f'Succesfully you have entered userID and Password')
else:
    print(f'OPP`s please enter the correct userID and Password')

captcha = random.randint(1111,9999)
print(captcha)

cap=int(input('Enter the captcha : '))
if(cap==captcha):
    print(f'Succesfully you Registered')
else:
    print(f'OPOO`s Fail!!!')    