#WAP to print the ODD number until n
n=int(input('Enter the number : '))
for i in range(1,n+1):
    if(i%2!=0):
        print(f'{i}')
