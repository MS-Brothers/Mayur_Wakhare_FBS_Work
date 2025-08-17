for i in range(1,6):
    for j in range(1,i+1):
        if(j==1):
            print('1',end=' ')
        elif(i==5):
            print(j,end=' ')
        elif(i==j):
            print(i,end='')
        else:
            print('  ',end='')        
    print()        
