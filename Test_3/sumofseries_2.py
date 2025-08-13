#Sum of series 
#1/1!+2/2!+3/3!

n=int(input('Enter the number :'))
sum =0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact *= j
    sum += i / fact 
print(sum)   
