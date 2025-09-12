#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
def freq(string):
    di={}
    word=string.split()
    for i in word:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    return di
string='mayur ramesh mayur'            
res=freq(string)
print(res)
