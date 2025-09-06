#Python Program to Form a New String where the First Character and the Last Character have been Exchanged
str='mayur'
if len(str)<=1:
    result=str
else:
    result=str[-1]+str[1:-1]+str[0]
print(str)
print(result)    

