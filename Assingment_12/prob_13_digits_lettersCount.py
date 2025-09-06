#Python Program to count number of digits and letters in a string.
def num(str):
    letter=0
    digit=0
    for i in str:
        if i>='a' and i<='z' or i>='A' and i<='Z':
            letter+=1
        if i>='0' and i<='9':
            digit+=1
    return letter,digit
str=input('Enter the string : ')
Letter,Digit=num(str)
print(f'Letter are {Letter} and Digits are {Digit}')            