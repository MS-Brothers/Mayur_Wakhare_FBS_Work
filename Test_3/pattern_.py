#Pattern 0,1 vala
for i in range(1,6):
    for j in range(1,6):
        if((i+j)%2 ==0):
            print(f'1',end='')
        else:
            print(f'0',end='')
    print()            
         