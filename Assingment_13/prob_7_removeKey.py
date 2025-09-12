#Python Program to Remove the Given Key from a Dictionary
def dict(di,numkey):
    key={}
    for i in di:
        if numkey != i:
            key[i]=di[i]
    return key
numkey=int(input('Enter the key : '))
di={1:23,2:'Mayur'}
res=dict(di,numkey)        
print(res)
