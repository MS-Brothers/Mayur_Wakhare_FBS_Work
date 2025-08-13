#to print first n prime numbers
n=int(input('Enter the number :'))
for i in range(1,n):
    if(i%2!=0):
        print(f'{i}')
        
