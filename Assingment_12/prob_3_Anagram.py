#Python Program to Detect if Two Strings are Anagrams
#1]lower case,space remove, new string madhe add karnar
def ana(str1,str2):
    s1=''
    for i in str1.lower():
        if str1 != ' ':
            s1+=i
    s2=''
    for i in str2.lower():
        if str2 != ' ':
            s2+=i


    if len(s1) != len(s2):
        return False


    for i in s1:
        count1 ,count2 = 0,0
        for j in s1:
            if i==j:
                count1+=1
        for j in s2:
            if i==j:
                count2+=1
        if count1 != count2:
            return False
    return True


str1=input('Enter the first string : ')
str2=input('Enter the Second string : ')

if(ana(str1,str2)):
    print("Anagram")
else:
    print('Not Anagram')    
