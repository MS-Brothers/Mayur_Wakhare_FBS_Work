#Python Program to replace every blank space with hyphen in a string.
def spa(str):
    s1=''
    for i in str:
        if i==" ":
            s1+='-'
        else:
            s1+=i
    return s1
str=input('Enter the string :')
res=spa(str)
print(res)            