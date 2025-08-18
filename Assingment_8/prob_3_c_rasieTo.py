#1^1 + 2^2 + 3^3+ ...... n^n
def rai(a):
    for i in range(1,a+1):
        b=i**i
    return b
a=int(input('Enter the number : '))    
res=rai(a)
print(f'{res}')

