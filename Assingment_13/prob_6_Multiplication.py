#Python Program to Multiply All the Items in a Dictionary
def dict(di):
    mul=1
    for i in di:
        mul*=di[i]
    return mul
dic={1:2,2:3,3:4}
res=dict(dic)
print(res)    