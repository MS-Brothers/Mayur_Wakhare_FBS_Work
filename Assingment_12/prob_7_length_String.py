#7. Python Program to Calculate the Length of a String Without Using a Library Function
def length(str):
    count=0
    for i in str:
        count+=1
    return count 
str=input('Enter the string : ')
res=length(str)
print(res)   