#Python Program to Take in a String and Replace Every Blank Space with Hyphen

def hyp(str):
    s1=''
    for i in str:
        if i==' ':
            s1+= '-'
        else:
            s1+=i    
    return s1        
str=input('Enter the string : ')

res=hyp(str)
print(res)