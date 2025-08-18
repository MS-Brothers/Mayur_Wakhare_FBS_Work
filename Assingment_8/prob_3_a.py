#1+ 2 + 3 + 4+..... + n
def series(sum):
    print(f'The sum of series is : {sum}')
n=int(input('Enter the number : '))
su=0
for i in range(1,n+1):
    su += i
series(su)    #in function calling you pass any parameter 
