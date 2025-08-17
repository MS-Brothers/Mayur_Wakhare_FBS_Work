for i in range(1,6):
    for j in range(1,6-i):
        print('',end=' ')
    for j in range(1,i+1):
        if( j==i or j==1 or i==5):
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()                