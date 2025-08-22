#Write a function to which we pass a parameter and print the factors of a given number For Eg: Factors of 12 : 1,2,3,4,6,12
def perf(a):
    for i in range(1,a):
        if(a%i==0):
            print(i,end=' ')

n=int(input('Enter the number : '))
perf(n)
print(n)
