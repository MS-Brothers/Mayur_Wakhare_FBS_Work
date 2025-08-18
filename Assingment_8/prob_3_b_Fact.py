#1!+ 2! + 3! + 4!+..... + n!
def factr(facto):
    print(f'The factorial is {facto}')
n=int(input('Enter the number : '))  
sum=0 
fact=1 
for i in range(1,n+1):
    fact*=i 
    sum+=fact   
factr(sum)    


