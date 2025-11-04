#Write a program to check if given number is Armstrong or not using recursive
# function.

#len(n) is wrong → n is a number, and len() works only on strings.
def arm(n,power):
    if n==0:
        return 0
    else:
        return (n%10)**power+arm(n//10,power)
n=int(input('Enter the number:'))    
power=len(str(n))# here we convert the int into str beacuse len() function not apply on integer
res=arm(n,power)

if res==n:
    print(f'{n} is Armstrong number.')
else:
    print(f'{n} is not Armstrong number.')    
        

