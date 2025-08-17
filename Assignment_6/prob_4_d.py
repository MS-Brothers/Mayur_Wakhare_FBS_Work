for i in range(1,6):
    for j in range(1,1+i):
        print(chr(64+j),end='')#Here only logic include j only
        #chr(65+i)
    print('') 

    # chr(64+i),end=''  => A
    #                     BB 
    #                     CCC 
    #                     DDDD