#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
def di(num):
    dict={}
    for i in range(1,num+1):
        dict[i]=i*i
    return dict    
num=int(input('Enter the number :' ))
res=di(num)
print(res)    