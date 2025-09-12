#Python Program to Sum All the Items in a Dictionary
def dict(di):
    total=0
    for i in di:
        total+=di[i]
    return total
di={1:12,2:34,3:45}
res=dict(di)
print(res)    
