#Sum of all prime numbers between 1 to n
def sumofPrime(n):
    count = 0
    num = 2
    total = 0
    while(count<n):
        for i in range (2, num):
            if (num % i == 0):
                break
        else:
            total += num
            count+=1
        num+=1
    print(f"Sum of Prime number = {total}")

n = int(input("Enter value of n = "))
sumofPrime(n)      
            