for i in range(1,6):
    for j in range(1,6-i):
        print(" " ,end='')
    # Resrart numbering for eact row    
    k=0    
    for j in range(1,i+1):
        print(chr(65+k),end=' ')
        k+=1
    for j in range(1,i):
        print(chr(65+k),end=' ')
        k+=1
    print('') 