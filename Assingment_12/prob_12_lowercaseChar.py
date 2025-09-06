#Python Program to count number of lowercase characters in a string.
def low(str):
    count=0
    for i in str:
        if i>='a' and i<='z':
            count+=1
    return count
str=input('Enter the String : ')
res=low(str)
print(res)        