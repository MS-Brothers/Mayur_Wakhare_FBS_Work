#Python Program to Sort the List According to the Second Element in Sublist
li=[[1,2],[45,78],[3,5],[9,8]]
for i in range(len(li)):
    for j in range(len(li)-i-1):
        if(li[j][1]>li[j+1][1]):
            li[j][1],li[j+1][1]=li[j+1][1],li[j][1]
print(li)            