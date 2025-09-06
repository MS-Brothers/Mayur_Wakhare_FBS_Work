#Python Program to Replace all Occurrences of ‘a’ with $ in a String
# str='Mayur is a very Good person'
# p=str.replace('a','$')
# print(p)

str='Mayur is a a a a  very good person'
new=''
for i in str:
    if i=='a':
        new+='$'
    else:
       new+=i  
print(new)         