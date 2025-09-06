#Python Program to Calculate the Number of Words and the Number of Characters Present in a String
# s = input("Enter the string: ")

# word_count = len(s.split())  
# char_count = len(s)
# print(word_count) 
# print(char_count)




def wor(str):
    char_cou=0
    for i in str:
        char_cou+=1
    word_cou=0
    for i in str:
        if i==" ":
            word_cou+=1
    word_cou+=1        
    return char_cou,word_cou
str=input('Enter the string : ')
char,word=wor(str)
print(f'Character : {char} Word : {word}')            
