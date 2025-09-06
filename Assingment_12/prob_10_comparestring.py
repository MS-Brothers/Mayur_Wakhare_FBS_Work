#10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
def s(str1,str2):
    s1=0
    for i in str1:
        s1+=1
    s2=0
    for i in str2:
        s2+=1
    if s1>s2:
        return str1
    elif s2>s1:
        return str2
    else:
        return 'Both strings are equal in length'

str1=input('Enter the string 1 : ')
str2=input('Enter the string 2 : ')
res=s(str1,str2)
print(res)            
