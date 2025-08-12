#WAP TO PRINT THE FIBONACII SERIES 
#0,1,1,2,3,5

# Using While loop
n=int(input('Enter how many numbers you want to print : '))
a=0
b=1
i=1
while(i<=n):
    c=a+b
    print(f'{c}')
    b=c
    a=b
    i+=1   


# Using For loop
# n=int(input('Enter how many numbers you want to print : '))
# a=1
# b=0
# for i in range(1,n):
#     c=a+b
#     print(f'{c}')
#     a=b
#     b=c






           