#Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition : a. Children below 12 = 30% discount b. Senior citizen (above 59) = 50% discount c. Others need to pay full.
n=int(input('Enter the number of Passengers : '))
for i in range(n):
    cost=float(input('Enter the cost : '))
    age = int(input('Enter you age plz : '))
    total_amt=0
    if(age<12):
        dis=cost*0.3
        print(f'Your total amount is {cost-dis}')
    elif(age>59):
        dis=cost*0.5
        print(f'Your total amount is {cost - dis}')
    else:
        print(f'Your total amount is {cost}')        
