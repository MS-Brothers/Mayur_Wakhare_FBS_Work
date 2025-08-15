#Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.
userid="Mayur"
pass_word='pass123'

for i in range(1,4):
    user_id=input('Enter the userid : ')
    pass_1=input('Enter the password : ')

    if(userid == user_id and pass_1 == pass_word):
       print(f'Login Succesfull')
       break
    
