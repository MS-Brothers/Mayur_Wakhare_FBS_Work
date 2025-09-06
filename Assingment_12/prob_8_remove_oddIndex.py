#Python Program to Remove the Characters of Odd Index Values in a String
def odd(str):
    s1=''
    for i in range(len(str)):
        if i%2==0:
            s1+=str[i]
    return s1
str=input('Enter the string : ')
res = odd(str)
print(res)        