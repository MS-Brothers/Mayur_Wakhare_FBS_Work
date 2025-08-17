# Hallow Square
for i in range(1,7):
    for j in range(1,6):
        if(i==6 or i==1 or j==5 or j==1):
            print(f'*',end =' ')
        else:
          print(f' ',end=' ')  
    print('')        