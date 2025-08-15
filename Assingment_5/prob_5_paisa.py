#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. (Use looping to optimize the problem)
amt=int(input('Enter the Amount : '))
notes=[2000,500,200,100,50,20,10] # We create a list as decending order because we want the minimum number of notes
for i in notes:# here i is go in list [notes] one by one
    if(amt>i):
        count=amt//i#2896//2000=1
        amt = amt % i#2896%2000= 896 remeaning amount we got
        print(f'{i} * {count} Notes')