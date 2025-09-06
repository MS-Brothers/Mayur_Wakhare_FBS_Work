#Python Program to Remove the nth Index Character from a Non-Empty String
str="Mayur Ramesh Wakhare"
def remove(n):
    result=''
    for i in range(len(str)):
        if i != n:
            result+=str[i]
    return result
n=int(input('Enter the index :'))
res=remove(n)
print(res)        

