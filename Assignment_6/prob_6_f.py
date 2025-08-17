#Pyramid
#k=1 we got series 
for i in range(1,6):
    for j in range(1,6-i):
        print(" " ,end='')
    # Resrart numbering for eact row    
    k=1    
    for j in range(1,i+1):
        print(k,end=' ')
        k+=1
    for j in range(1,i):
        print(k,end=' ')
        k+=1
    print('')            
