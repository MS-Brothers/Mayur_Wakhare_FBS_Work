def patte(n):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if(i==1 or i==n or i+j==n+1):
                    print('*',end=' ')
                
                else:
                    print(' ',end=' ')
            print()   
n = int(input("Enter the n:- "))
patte(n)          