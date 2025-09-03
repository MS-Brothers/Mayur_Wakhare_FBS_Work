#Python Program to Sort a List According to the Length of the Elements within the list.

li=[12,'mayur',569,'op']
for i in range(len(li)):
    for j in range(len(li)-i-1):
        if(len(str(li[j])) > len(str(li[j+1]))):
            li[j],li[j+1]= li[j+1],li[j]
print(li)            
