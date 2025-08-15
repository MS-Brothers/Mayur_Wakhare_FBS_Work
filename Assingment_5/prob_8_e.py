#x - x2/3 + x3/5 - x4/7 + .... to n terms
n=int(input('Enter the value of n : '))
x=int(input('Enter the value of x : '))
sum=0
for i in range(1,n+1):
    term = x*i/(2*i-1)
    if(i%2==0):
        sum -= term
    else:
        sum += term
print(f'{sum}')            