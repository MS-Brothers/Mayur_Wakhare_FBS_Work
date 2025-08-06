#Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition : a. Children below 12 = 30% discount b. Senior citizen (above 59) = 50% discount c. Others need to pay full.
age = int(input('Enter your age : '))
ticket = int(input('Enter your ticket : '))
to_tic =0
if(age < 12):
    to_tic = ticket *0.3
elif(age > 59):
    to_tic=ticket*0.5
else:
    ticket = ticket

print(f'Total Ticket Amount {ticket - to_tic}')